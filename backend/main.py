"""
MuseBoard Backend API
FastAPI server for AI-powered ad generation and management
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import json
from datetime import datetime
import os

app = FastAPI(title="MuseBoard API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DB_PATH = "museboard.db"

def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL,
            format TEXT NOT NULL,
            tone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            views INTEGER DEFAULT 0,
            likes INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Pydantic models
class AdGenerationRequest(BaseModel):
    product_description: str
    category: str = "general"
    format: str = "social_media"
    tone: str = "persuasive"

class Ad(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    category: str
    format: str
    tone: Optional[str] = None
    created_at: Optional[str] = None
    views: int = 0
    likes: int = 0

# Template-based ad generation
def generate_ad_template(request: AdGenerationRequest) -> dict:
    """Generate ad using templates"""
    templates = {
        "restaurant": {
            "title": f"Savor the Flavor: {request.product_description[:30]}",
            "content": f"Experience the taste of {request.product_description}! Fresh ingredients, authentic flavors, and unforgettable moments await. Book your table today and discover why we're the talk of the town. 🍽️ BOOK NOW"
        },
        "fashion": {
            "title": f"Step Into Style: {request.product_description[:30]}",
            "content": f"Elevate your wardrobe with {request.product_description}. Trendsetting designs that make you stand out. Limited collection available. Express yourself through fashion. 👗 SHOP NOW"
        },
        "tech": {
            "title": f"Innovate Today: {request.product_description[:30]}",
            "content": f"Transform your workflow with {request.product_description}. Cutting-edge technology meets intuitive design. Join thousands of satisfied users who've made the switch. 💻 GET STARTED"
        },
        "courses": {
            "title": f"Master New Skills: {request.product_description[:30]}",
            "content": f"Unlock your potential with {request.product_description}. Expert-led courses designed for real-world success. Start learning today and advance your career. 📚 ENROLL NOW"
        }
    }
    
    template = templates.get(request.category, {
        "title": f"Discover: {request.product_description[:40]}",
        "content": f"Don't miss out on {request.product_description}! Limited time offer. Act now and experience the difference. ✨ LEARN MORE"
    })
    
    return template

# API Endpoints
@app.get("/")
def root():
    return {
        "message": "MuseBoard API - The Billboard for the AI-Made World",
        "version": "1.0.0",
        "endpoints": {
            "generate": "/api/ads/generate",
            "list": "/api/ads",
            "detail": "/api/ads/{id}",
            "like": "/api/ads/{id}/like"
        }
    }

@app.post("/api/ads/generate", response_model=Ad)
def generate_ad(request: AdGenerationRequest):
    """Generate a new ad and save to database"""
    
    # Generate ad content
    ad_data = generate_ad_template(request)
    
    # Save to database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ads (title, content, category, format, tone) VALUES (?, ?, ?, ?, ?)",
        (ad_data["title"], ad_data["content"], request.category, request.format, request.tone)
    )
    conn.commit()
    ad_id = cursor.lastrowid
    
    # Get the created ad
    cursor.execute("SELECT * FROM ads WHERE id = ?", (ad_id,))
    row = cursor.fetchone()
    conn.close()
    
    return Ad(
        id=row[0],
        title=row[1],
        content=row[2],
        category=row[3],
        format=row[4],
        tone=row[5],
        created_at=row[6],
        views=row[7],
        likes=row[8]
    )

@app.get("/api/ads", response_model=List[Ad])
def get_ads(limit: int = 50, category: Optional[str] = None):
    """Get all ads from the board"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if category and category != "all":
        cursor.execute(
            "SELECT * FROM ads WHERE category = ? ORDER BY created_at DESC LIMIT ?",
            (category, limit)
        )
    else:
        cursor.execute("SELECT * FROM ads ORDER BY created_at DESC LIMIT ?", (limit,))
    
    rows = cursor.fetchall()
    conn.close()
    
    ads = []
    for row in rows:
        ads.append(Ad(
            id=row[0],
            title=row[1],
            content=row[2],
            category=row[3],
            format=row[4],
            tone=row[5],
            created_at=row[6],
            views=row[7],
            likes=row[8]
        ))
    
    return ads

@app.get("/api/ads/{ad_id}", response_model=Ad)
def get_ad(ad_id: int):
    """Get a specific ad by ID"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ads WHERE id = ?", (ad_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Ad not found")
    
    # Increment view count
    cursor.execute("UPDATE ads SET views = views + 1 WHERE id = ?", (ad_id,))
    conn.commit()
    conn.close()
    
    return Ad(
        id=row[0],
        title=row[1],
        content=row[2],
        category=row[3],
        format=row[4],
        tone=row[5],
        created_at=row[6],
        views=row[7] + 1,
        likes=row[8]
    )

@app.post("/api/ads/{ad_id}/like")
def like_ad(ad_id: int):
    """Increment like count for an ad"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE ads SET likes = likes + 1 WHERE id = ?", (ad_id,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Ad not found")
    
    conn.commit()
    cursor.execute("SELECT likes FROM ads WHERE id = ?", (ad_id,))
    likes = cursor.fetchone()[0]
    conn.close()
    
    return {"likes": likes}

@app.delete("/api/ads/{ad_id}")
def delete_ad(ad_id: int):
    """Delete an ad from the board"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ads WHERE id = ?", (ad_id,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Ad not found")
    
    conn.commit()
    conn.close()
    
    return {"message": "Ad deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
