# MuseBoard Deployment Guide

## ✅ Code is Ready!

Your MuseBoard application is built and committed to Git. Here's how to deploy it:

## 🚀 Deploy to Vercel (Frontend)

### Option 1: Using Vercel CLI (Recommended)

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
cd /Users/knelyo/museboard/frontend
vercel --prod
```

### Option 2: Using Vercel Website

1. Push your code to GitHub:
   - Go to https://github.com/new
   - Create a new repository named "museboard"
   - Run these commands:
   ```bash
   cd /Users/knelyo/museboard
   git remote add origin https://github.com/knelyoo/museboard.git
   git branch -M main
   git push -u origin main
   ```

2. Deploy to Vercel:
   - Go to https://vercel.com/new
   - Import your GitHub repository
   - Set Root Directory to: `frontend`
   - Click "Deploy"

## 🗄️ Deploy Backend (Railway/Render)

### Option 1: Railway (Recommended)

1. Go to https://railway.app/
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your museboard repository
4. Set Root Directory to: `backend`
5. Railway will auto-detect Python and deploy

### Option 2: Render

1. Go to https://render.com/
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - Name: museboard-api
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"

## 🔗 After Deployment

Once deployed, update the API URL in your frontend:

```bash
# frontend/.env.local
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
```

Then redeploy the frontend.

## 📝 Repository Structure

```
museboard/
├── backend/           # FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   ├── Procfile
│   └── runtime.txt
├── frontend/          # Next.js frontend
│   ├── app/
│   ├── components/
│   └── package.json
└── README.md
```

## 🎉 You're Done!

Your MuseBoard is ready to share with the world!

Visit your deployed site and start creating AI-powered ads!
