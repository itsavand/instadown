# Quick Start: Enable Stories & Update GitHub

## 🎯 Part 1: Enable Instagram Stories (with cookies.txt)

### **Step 1: Export Instagram Cookies**

1. Install browser extension:
   - Chrome: https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc

2. Log into Instagram in your browser

3. Click extension → Export cookies for instagram.com

4. Save as `cookies.txt` in your bot folder:
   ```bash
   ~/Desktop/insta vid st down/cookies.txt
   ```

### **Step 2: Upload to Railway**

**Option A: Using Railway CLI (Recommended)**
```bash
cd ~/Desktop/insta\ vid\ st\ down
railway login
railway link  # Select your project
railway up    # Uploads cookies.txt
```

**Option B: Via GitHub (if connected)**
```bash
# Temporarily allow cookies.txt in git
nano .gitignore
# Comment out line 5: # cookies.txt

git add cookies.txt
git commit -m "Add cookies for stories"
git push origin main

# Railway auto-deploys with cookies
```

⚠️ **Security Warning:** Only use Option B if your GitHub repo is PRIVATE!

---

## 🔄 Part 2: Update GitHub Repository

### **Quick Commands:**

```bash
# Navigate to project
cd ~/Desktop/insta\ vid\ st\ down

# Check what changed
git status

# Add all changes
git add .

# Commit with message
git commit -m "Updated bot code"

# Push to GitHub
git push origin main
```

### **Railway Auto-Deploy:**
- Railway detects GitHub push
- Automatically rebuilds and deploys
- Bot restarts with new code (1-2 minutes)

---

## 📋 Complete Workflow Example

```bash
# 1. Make changes to code
nano main.py

# 2. Test locally (optional)
python3 main.py
# Press Ctrl+C to stop

# 3. Add changes to git
git add main.py requirements.txt

# 4. Commit
git commit -m "Fixed story downloads"

# 5. Push to GitHub
git push origin main

# 6. Wait for Railway to auto-deploy
# Check Railway dashboard → Deployments tab
```

---

## ✅ Verify Stories Work

1. **Check Railway Logs:**
   - Railway dashboard → Your service → Deployments
   - Look for: `Using cookies file: cookies.txt`

2. **Test in Telegram:**
   - Send a story link to your bot
   - Should download successfully! 🎉

---

## 🔐 Important Security Notes

**Protected by .gitignore (won't be uploaded to GitHub):**
- ✅ `.env` (your credentials)
- ✅ `cookies.txt` (your Instagram session)
- ✅ `*.session` files
- ✅ `downloads/` folder

**Safe to upload to GitHub:**
- ✅ `main.py`
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `README.md`
- ✅ All guide files

---

## 🚨 Troubleshooting

### Stories still don't work?
```bash
# 1. Check Railway logs
# 2. Re-export fresh cookies
# 3. Upload again with: railway up
# 4. Wait for auto-deploy
```

### Can't push to GitHub?
```bash
# Use HTTPS instead of SSH
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push origin main
```

### Railway not auto-deploying?
1. Check Railway settings → Enable "Auto-deploy"
2. Make sure GitHub is connected
3. Check deployment logs for errors

---

## 📞 Need More Details?

See the complete guides:
- `RAILWAY_COOKIES_GUIDE.md` - Full cookie setup
- `GITHUB_UPDATE_GUIDE.md` - Complete Git workflow
