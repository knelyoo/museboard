# 🚀 MuseBoard Deployment Instructions

## ✅ What's Been Built

Your complete **MuseBoard** application is ready! Here's what was created:

### 📁 Project Structure
```
museboard/
├── backend/                    # FastAPI Python backend
│   ├── main.py                # API with all endpoints
│   ├── requirements.txt       # Python dependencies
│   ├── Procfile              # For Railway/Heroku deployment
│   └── runtime.txt           # Python version
├── frontend/                  # Next.js React frontend
│   ├── app/
│   │   ├── page.tsx          # Main MuseBoard page
│   │   ├── layout.tsx        # Root layout with metadata
│   │   └── globals.css       # Global styles
│   ├── components/
│   │   ├── AdCard.tsx        # Individual ad display
│   │   ├── HeroAd.tsx        # Featured ad display
│   │   └── AdGenerator.tsx   # Ad creation form
│   ├── package.json          # Node dependencies
│   └── .env.local            # Environment variables
├── README.md                  # Project documentation
└── .gitignore                # Git ignore rules
```

### 🎨 Features Implemented

✅ **Backend (FastAPI)**
- RESTful API with 6 endpoints
- SQLite database for ad storage
- Template-based ad generation (ready for AI integration)
- CORS enabled for frontend communication

✅ **Frontend (Next.js + React + TypeScript)**
- Dark-themed, responsive design
- Hero featured ad section
- Grid layout for latest ads
- Category filtering (Restaurant, Fashion, Tech, Courses)
- Like and view tracking
- Real-time updates (auto-refresh)
- Ad generation form with multiple options

✅ **Design System**
- Color palette: Dark slate background (#0F172A)
- Accent color: Amber (#F59E0B)
- Category-specific colors
- Tailwind CSS utilities
- Micro-interactions and hover effects

---

## 📋 Deployment Steps

### Step 1: Push to GitHub

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Repository name: `museboard`
   - Description: "AI-powered billboard application built with Model Spec principles"
   - Make it Public
   - Click "Create repository"

2. **Push your code:**
   ```bash
   cd /Users/knelyo/museboard
   git remote add origin https://github.com/knelyoo/museboard.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy Backend to Railway

1. **Go to Railway:**
   - Visit https://railway.app/
   - Sign in with GitHub

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `museboard` repository
   - Click on the created service

3. **Configure Service:**
   - Go to "Settings"
   - Set "Root Directory" to: `backend`
   - Railway auto-detects Python and runs: `uvicorn main:app`
   - Note your deployment URL (e.g., `https://museboard-production-xxxx.up.railway.app`)

4. **Enable Public Networking:**
   - In Settings → "Networking"
   - Click "Generate Domain"
   - Save your API URL

### Step 3: Deploy Frontend to Vercel

#### Option A: Using Vercel CLI (Fast)

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
cd /Users/knelyo/museboard/frontend
vercel --prod
```

When prompted:
- Set up and deploy? → Yes
- Which scope? → Your account
- Link to existing project? → No
- Project name? → museboard (or your choice)
- Directory? → `./` (current directory)
- Override settings? → No

#### Option B: Using Vercel Website

1. **Go to Vercel:**
   - Visit https://vercel.com/new
   - Sign in with GitHub

2. **Import Repository:**
   - Click "Import Project"
   - Select your `museboard` repository
   - Click "Import"

3. **Configure Project:**
   - Framework Preset: Next.js (auto-detected)
   - Root Directory: `frontend`
   - Build Command: `npm run build` (default)
   - Output Directory: `.next` (default)

4. **Add Environment Variable:**
   - Click "Environment Variables"
   - Add: `NEXT_PUBLIC_API_URL` = `https://your-railway-url.up.railway.app`
   - Click "Deploy"

### Step 4: Update Frontend with Backend URL

After Railway deployment:

```bash
# Update frontend/.env.local
NEXT_PUBLIC_API_URL=https://your-actual-railway-url.up.railway.app
```

Then redeploy on Vercel:
```bash
cd /Users/knelyo/museboard/frontend
vercel --prod
```

Or push to GitHub and Vercel will auto-deploy.

---

## 🧪 Testing Your Deployment

### Test Backend API

```bash
# Check API is running
curl https://your-railway-url.up.railway.app/

# Expected response:
# {"message": "MuseBoard API - The Billboard for the AI-Made World", ...}
```

### Test Frontend

1. Visit your Vercel URL (e.g., `https://museboard.vercel.app`)
2. Click "+ Create Ad"
3. Fill in:
   - Product description: "A new Italian restaurant in downtown"
   - Category: Restaurant
   - Format: Social Media
   - Tone: Persuasive
4. Click "Generate Ad"
5. Should see new ad appear on the board!

### Test Features

- ✅ Category filtering works
- ✅ Like button increments count
- ✅ View count increases when viewing ads
- ✅ Hero featured ad displays
- ✅ Responsive design on mobile
- ✅ Real-time updates (wait 30s for auto-refresh)

---

## 🐛 Troubleshooting

### Backend Issues

**Problem:** Railway deployment fails
- **Solution:** Check `backend/runtime.txt` has correct Python version
- Check logs in Railway dashboard

**Problem:** CORS errors in browser console
- **Solution:** Backend allows all origins (`allow_origins=["*"]`)
- If needed, update to specific domain in `main.py`

**Problem:** Database not persisting
- **Solution:** Railway provides persistent storage
- SQLite file will be created on first run

### Frontend Issues

**Problem:** "Failed to fetch ads"
- **Solution:** Check `NEXT_PUBLIC_API_URL` is set correctly
- Verify backend is running and accessible

**Problem:** Build fails on Vercel
- **Solution:** Ensure Node version >=20.9.0 in Vercel settings
- Check all dependencies are in `package.json`

**Problem:** Components not found
- **Solution:** Verify import paths use `@/components/`
- Check `tsconfig.json` has correct path mapping

---

## 📊 Monitoring & Analytics

### Railway Dashboard
- View API logs
- Monitor CPU/Memory usage
- Check request volume

### Vercel Dashboard
- View deployment logs
- Monitor page performance
- Check build status

---

## 🔧 Local Development

### Backend
```bash
cd /Users/knelyo/museboard/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
# Runs on http://localhost:8000
```

### Frontend
```bash
cd /Users/knelyo/museboard/frontend
npm install
npm run dev
# Runs on http://localhost:3000
```

---

## 🎉 Success!

Once deployed:

1. **Your Frontend URL:** `https://museboard-[your-id].vercel.app`
2. **Your Backend URL:** `https://museboard-production-[hash].up.railway.app`

Share your MuseBoard with the world! 🚀

---

## 📝 Next Steps (Optional)

1. **Add AI Integration:**
   - Sign up for Anthropic API key
   - Add to Railway environment variables
   - Ads will use Claude for generation

2. **Custom Domain:**
   - Add custom domain in Vercel settings
   - Update DNS records

3. **Analytics:**
   - Add Vercel Analytics
   - Track user engagement

4. **Enhancements:**
   - Add user authentication
   - Implement WebSocket for real-time updates
   - Add image generation for ads
   - Create admin dashboard

---

**Built with ❤️ using the Model Spec Framework**

*"The most valuable artifact isn't code—it's structured communication."*
