# Create GitHub Repository

Since the repository doesn't exist yet, follow these steps:

## Option 1: Using GitHub Website (Easiest)

1. **Go to GitHub:**
   - Visit https://github.com/new
   - Login with your GitHub account

2. **Create Repository:**
   - Repository name: `museboard`
   - Description: "AI-powered billboard application - MuseBoard™"
   - Make it **Public** ✅
   - ❌ Do NOT initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

3. **Push Your Code:**
   ```bash
   cd /Users/knelyo/museboard
   git remote add origin https://github.com/knelyoo/museboard.git
   git branch -M main
   git push -u origin main
   ```

## Option 2: Using GitHub CLI (if installed)

```bash
# Install GitHub CLI (if not installed)
brew install gh

# Login
gh auth login

# Create repo and push
cd /Users/knelyo/museboard
gh repo create museboard --public --source=. --remote=origin --push
```

## After Pushing

Once the code is on GitHub, you can:

1. **Deploy Backend on Railway:**
   - https://railway.app/
   - New Project → Deploy from GitHub
   - Select `museboard` repo
   - Set root directory: `backend`

2. **Deploy Frontend on Vercel:**
   - https://vercel.com/new
   - Import `museboard` repo
   - Set root directory: `frontend`
   - Add environment variable: `NEXT_PUBLIC_API_URL` = your Railway URL

---

**Quick Summary:**
1. Create repo at https://github.com/new (name: museboard)
2. Run the git commands above to push
3. Deploy on Railway (backend) and Vercel (frontend)
