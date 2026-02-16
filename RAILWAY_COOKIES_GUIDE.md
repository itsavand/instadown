# How to Enable Instagram Stories on Railway

## 📋 Overview

To download Instagram stories, you need to upload your Instagram cookies to Railway. Here's how:

---

## Step 1: Export Your Instagram Cookies

### **Method 1: Using Browser Extension (Easiest)**

1. **Install Cookie Extension:**
   - **Chrome:** [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - **Firefox:** [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

2. **Log into Instagram:**
   - Go to https://instagram.com
   - Make sure you're logged in

3. **Export Cookies:**
   - Click the extension icon
   - Select "instagram.com"
   - Click "Export" or "Download"
   - Save as `cookies.txt`

### **Method 2: Using yt-dlp (Advanced)**

```bash
cd ~/Desktop/insta\ vid\ st\ down
yt-dlp --cookies-from-browser chrome --cookies cookies.txt "https://www.instagram.com/"
```

---

## Step 2: Upload cookies.txt to Railway

### **Option A: Using Railway CLI (Recommended)**

1. **Make sure cookies.txt is in your project folder:**
   ```bash
   cd ~/Desktop/insta\ vid\ st\ down
   ls cookies.txt  # Should show the file
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Link to your project:**
   ```bash
   railway link
   ```
   Select your Instagram bot project

4. **Upload the file:**
   ```bash
   railway up
   ```
   
   This will upload ALL files including cookies.txt

### **Option B: Using Railway Dashboard (Manual)**

Unfortunately, Railway doesn't have a direct file upload feature in the dashboard. You MUST use one of these methods:

1. **Railway CLI** (recommended - see Option A above)
2. **GitHub** (see Step 3 below)
3. **Environment Variable** (for small cookies - not recommended)

---

## Step 3: Upload via GitHub (Alternative)

If you've uploaded your code to GitHub:

1. **Add cookies.txt to your repository:**
   ```bash
   cd ~/Desktop/insta\ vid\ st\ down
   
   # IMPORTANT: Remove cookies.txt from .gitignore temporarily
   nano .gitignore
   # Comment out or remove the line: cookies.txt
   
   git add cookies.txt
   git commit -m "Add cookies for story downloads"
   git push
   ```

2. **Railway will auto-deploy** with the new cookies.txt file

3. **⚠️ SECURITY WARNING:**
   - Your cookies.txt will be PUBLIC on GitHub
   - Anyone can use your Instagram session
   - **Only do this if your repo is PRIVATE**

---

## Step 4: Verify It's Working

1. **Check Railway Logs:**
   - Go to Railway dashboard
   - Click on your service
   - Click "Deployments"
   - Look for: `Using cookies file: cookies.txt`

2. **Test with a Story:**
   - Send your bot a story link
   - It should now download successfully!

---

## 🔒 Security Best Practices

### **DO:**
- ✅ Use a PRIVATE GitHub repository
- ✅ Regenerate cookies every 30-90 days
- ✅ Use Railway CLI to upload cookies

### **DON'T:**
- ❌ Upload cookies to PUBLIC GitHub repo
- ❌ Share your cookies.txt file
- ❌ Commit cookies to version control (if repo is public)

---

## 🔄 Updating Cookies When They Expire

Cookies expire after 30-90 days. When they do:

1. Export fresh cookies from your browser
2. Upload to Railway using Railway CLI:
   ```bash
   railway up
   ```
3. Railway will auto-restart with new cookies

---

## ⚠️ Important Notes

- **Cookies are tied to your Instagram account**
- **If you change your Instagram password, cookies expire**
- **If you log out of Instagram, cookies expire**
- **Keep cookies.txt secure - it's like your password**

---

## 📊 What Will Work After Setup

| Content Type | Before Cookies | After Cookies |
|--------------|----------------|---------------|
| Reels | ✅ Works | ✅ Works |
| Posts | ✅ Works | ✅ Works |
| Stories | ❌ Fails | ✅ **Works!** |
| Private Content | ❌ Fails | ✅ **Works!** |

---

## 🚀 Quick Summary

1. Export cookies from browser → `cookies.txt`
2. Upload to Railway using `railway up`
3. Railway auto-restarts with cookies
4. Stories now work! 🎉

---

## Need Help?

If stories still don't work:
- Check Railway logs for "Using cookies file"
- Make sure cookies.txt is in Netscape format
- Try exporting fresh cookies
- Verify you're logged into Instagram
