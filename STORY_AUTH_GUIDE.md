# Instagram Story Authentication Guide

## 🔐 Why Stories Need Authentication

Instagram **requires authentication** to download stories, even public ones. This is different from posts and reels which can be downloaded without logging in.

## ✅ Solution: Automatic Browser Cookie Extraction

I've updated your bot to **automatically extract cookies** from your browser! This is the easiest method.

### **How It Works:**

1. **Make sure you're logged into Instagram** in one of these browsers:
   - **Chrome** (recommended)
   - **Firefox**
   - **Safari**

2. **The bot will automatically use your cookies** when downloading stories

3. **No manual cookie export needed!**

---

## 🚀 Quick Test

1. Open Chrome/Firefox/Safari
2. Go to instagram.com and make sure you're logged in
3. Send a story link to your bot
4. The bot should now be able to download it!

---

## 🔧 Alternative: Manual Cookie Export (If Automatic Doesn't Work)

If the automatic method doesn't work, you can manually export cookies:

### **Method 1: Using Browser Extension (Easiest)**

1. **Install a cookie export extension:**
   - **Chrome/Edge:** [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - **Firefox:** [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

2. **Log into Instagram** in your browser

3. **Click the extension icon** and select instagram.com

4. **Export cookies** and save as `cookies.txt`

5. **Place the file** in your bot directory:
   ```
   ~/Desktop/insta vid st down/cookies.txt
   ```

6. **Restart the bot:**
   ```bash
   # Stop the bot (Ctrl+C in the terminal)
   python3 main.py
   ```

### **Method 2: Using yt-dlp Command (Advanced)**

You can also use yt-dlp's built-in cookie extraction:

```bash
cd ~/Desktop/insta\ vid\ st\ down
yt-dlp --cookies-from-browser chrome --cookies cookies.txt "https://www.instagram.com/"
```

This will extract cookies from Chrome and save them to `cookies.txt`.

---

## ⚠️ Important Notes

### **Cookie Expiration**
- Cookies expire after some time (usually 30-90 days)
- If downloads stop working, re-export your cookies
- The bot will tell you if authentication fails

### **Security**
- **Never share your cookies.txt file** - it contains your Instagram session
- Keep the file in your bot directory only
- The `.gitignore` file protects it from being uploaded to GitHub

### **Browser Requirements**
- You must be logged into Instagram in the browser
- The browser must be on the same computer as the bot
- Close the browser before exporting cookies (for some methods)

---

## 🐛 Troubleshooting

### "Story download failed - authentication required"
✅ **Solution:** Make sure you're logged into Instagram in Chrome/Firefox/Safari

### "No cookies available"
✅ **Solution:** 
1. Log into Instagram in your browser
2. OR manually export cookies.txt
3. Restart the bot

### "Cookies expired"
✅ **Solution:** Re-export fresh cookies from your browser

### Bot still can't download stories
✅ **Try this:**
1. Log out of Instagram in your browser
2. Log back in
3. Export fresh cookies
4. Restart the bot

---

## 📊 What Works Without Cookies

| Content Type | Requires Cookies? |
|--------------|-------------------|
| Posts (videos) | ❌ No |
| Reels | ❌ No |
| Stories | ✅ **Yes** |
| Private accounts | ✅ Yes |

---

## 🎯 Recommended Setup

**For best results:**

1. **Use Chrome browser**
2. **Stay logged into Instagram**
3. **Let the bot auto-extract cookies**
4. **If that fails, manually export cookies.txt**

The bot will prioritize:
1. Manual `cookies.txt` file (if exists)
2. Chrome browser cookies
3. Firefox browser cookies  
4. Safari browser cookies

---

## ✅ Current Bot Status

Your bot is now configured to:
- ✅ Automatically try to extract cookies from Chrome
- ✅ Fall back to Firefox if Chrome fails
- ✅ Fall back to Safari if Firefox fails
- ✅ Use manual cookies.txt if provided
- ✅ Give clear error messages if authentication fails

**Try sending a story link now!** 🚀
