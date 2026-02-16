# How to Update Your GitHub Repository

## 🔄 Complete GitHub Update Workflow

---

## First Time Setup (If Not Done Yet)

### **Step 1: Initialize Git Repository**

```bash
cd ~/Desktop/insta\ vid\ st\ down

# Initialize git (if not already done)
git init

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

---

## Updating Files on GitHub

### **Step 1: Check What Changed**

```bash
cd ~/Desktop/insta\ vid\ st\ down

# See what files have changed
git status
```

### **Step 2: Add Files to Commit**

**Option A: Add All Changed Files**
```bash
git add .
```

**Option B: Add Specific Files Only**
```bash
# Add only the files you want to update
git add main.py
git add requirements.txt
git add Procfile
```

**⚠️ IMPORTANT: Don't Add Sensitive Files**
```bash
# Make sure .gitignore is working
cat .gitignore

# These should NOT be added:
# - .env (contains your credentials)
# - cookies.txt (contains your Instagram session)
# - *.session files
```

### **Step 3: Commit Changes**

```bash
git commit -m "Updated bot code - fixed cookie handling"
```

### **Step 4: Push to GitHub**

```bash
git push origin main
```

Or if your default branch is `master`:
```bash
git push origin master
```

---

## 🔄 Auto-Deploy to Railway from GitHub

### **Step 1: Connect Railway to GitHub**

1. Go to Railway dashboard
2. Click on your service
3. Click **"Settings"**
4. Under **"Service Source"**, click **"Connect to GitHub"**
5. Authorize Railway to access your GitHub
6. Select your repository

### **Step 2: Enable Auto-Deploy**

1. In Railway settings, find **"Deployments"**
2. Make sure **"Auto-deploy"** is enabled
3. Select the branch (usually `main` or `master`)

### **Step 3: How It Works**

Now, whenever you push to GitHub:
1. ✅ GitHub receives your changes
2. ✅ Railway detects the update
3. ✅ Railway automatically rebuilds and deploys
4. ✅ Your bot restarts with new code

---

## 📋 Complete Update Workflow

### **Every Time You Make Changes:**

```bash
# 1. Navigate to your project
cd ~/Desktop/insta\ vid\ st\ down

# 2. Check what changed
git status

# 3. Add changed files
git add main.py requirements.txt Procfile

# 4. Commit with a message
git commit -m "Describe what you changed"

# 5. Push to GitHub
git push origin main

# 6. Railway auto-deploys (wait 1-2 minutes)
```

---

## 🔐 Protecting Sensitive Files

### **Your .gitignore Should Include:**

```
# Environment variables
.env

# Instagram cookies (sensitive)
cookies.txt

# Pyrogram session files
*.session
*.session-journal

# Download directory
downloads/

# Python
__pycache__/
*.pyc
```

### **Verify .gitignore is Working:**

```bash
# This should NOT show .env or cookies.txt
git status
```

---

## 🚀 Quick Commands Reference

| Task | Command |
|------|---------|
| Check status | `git status` |
| Add all files | `git add .` |
| Add specific file | `git add filename` |
| Commit changes | `git commit -m "message"` |
| Push to GitHub | `git push origin main` |
| Pull from GitHub | `git pull origin main` |
| View commit history | `git log` |

---

## 🔄 Updating Specific Files

### **Update Only Code Files:**
```bash
git add main.py
git commit -m "Fixed story download feature"
git push origin main
```

### **Update Dependencies:**
```bash
git add requirements.txt
git commit -m "Updated dependencies"
git push origin main
```

### **Update Configuration:**
```bash
git add Procfile render.yaml
git commit -m "Updated deployment config"
git push origin main
```

---

## ⚠️ Common Issues

### **"Permission denied (publickey)"**
You need to set up SSH keys or use HTTPS with personal access token.

**Quick fix - Use HTTPS:**
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### **"Updates were rejected"**
Someone else pushed changes. Pull first:
```bash
git pull origin main
git push origin main
```

### **"Merge conflict"**
Resolve conflicts manually, then:
```bash
git add .
git commit -m "Resolved merge conflict"
git push origin main
```

---

## 🎯 Best Practices

1. **Commit often** with clear messages
2. **Never commit** `.env` or `cookies.txt`
3. **Test locally** before pushing
4. **Use meaningful commit messages**
5. **Keep .gitignore updated**

---

## 📊 Complete Example Workflow

```bash
# 1. Make changes to your code
nano main.py

# 2. Test locally
python3 main.py

# 3. Stop local bot (Ctrl+C)

# 4. Add changes
git add main.py

# 5. Commit
git commit -m "Added better error handling for stories"

# 6. Push to GitHub
git push origin main

# 7. Wait for Railway to auto-deploy (1-2 minutes)

# 8. Check Railway logs to verify deployment
```

---

## ✅ Summary

**To update your bot:**
1. Make changes locally
2. Test them
3. `git add` → `git commit` → `git push`
4. Railway auto-deploys from GitHub
5. Done! 🎉

**Remember:**
- ❌ Never commit `.env` or `cookies.txt`
- ✅ Always test locally first
- ✅ Use clear commit messages
- ✅ Let Railway auto-deploy from GitHub
