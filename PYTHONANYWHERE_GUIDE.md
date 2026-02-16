# Quick Deploy to PythonAnywhere - Step by Step

## ⚠️ Warning
PythonAnywhere **free tier does NOT support always-on bots**. Your bot will stop when:
- You close the browser
- After 3 months of inactivity
- The console times out

**For 24/7 hosting, use Railway.app instead (see DEPLOYMENT_GUIDE.md)**

---

## Step-by-Step Instructions for PythonAnywhere

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com
2. Click **"Start running Python online in less than a minute"**
3. Create a free account (Beginner account)
4. Verify your email

### Step 2: Open a Bash Console
1. After logging in, click on **"Consoles"** tab
2. Click **"Bash"** to start a new bash console

### Step 3: Upload Your Files

**Option A: Upload via Web Interface (Easier)**
1. Click on **"Files"** tab
2. Click **"Upload a file"**
3. Upload these files one by one:
   - `main.py`
   - `requirements.txt`
   - `.env`

**Option B: Use Git (If you have GitHub)**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

**Option C: Manual Upload via Console**
1. In the Bash console, create directory:
```bash
mkdir instagram_bot
cd instagram_bot
```

2. Create files manually:
```bash
nano main.py
# Paste your main.py content, then Ctrl+X, Y, Enter

nano requirements.txt
# Paste your requirements.txt content, then Ctrl+X, Y, Enter

nano .env
# Paste your .env content, then Ctrl+X, Y, Enter
```

### Step 4: Install Dependencies

In the Bash console:
```bash
cd ~/instagram_bot
pip3 install --user -r requirements.txt
```

Wait for installation to complete (2-3 minutes).

### Step 5: Run the Bot

```bash
python3 main.py
```

You should see:
```
Starting Instagram Downloader Bot...
Download directory: /home/yourusername/instagram_bot/downloads
Session started
```

### Step 6: Test Your Bot

1. Open Telegram
2. Search for your bot
3. Send `/start`
4. Send an Instagram reel link
5. Bot should download and send the video

---

## ⚠️ IMPORTANT LIMITATIONS

### Free Account Limitations:
- ❌ Bot stops when you close the browser
- ❌ No always-on tasks
- ❌ Limited CPU time (100 seconds/day)
- ❌ Restricted outbound internet access
- ❌ Console times out after inactivity

### Paid Account ($5/month):
- ✅ Always-on tasks available
- ✅ More CPU time
- ✅ Better internet access
- ✅ Can run 24/7

---

## Files to Upload

### ✅ Required Files:
```
main.py          ← Your bot code
requirements.txt ← Dependencies
.env            ← Your credentials (API_ID, API_HASH, BOT_TOKEN)
```

### ❌ DO NOT Upload:
```
.gitignore       ← Not needed
README.md        ← Optional
STORY_AUTH_GUIDE.md ← Optional
downloads/       ← Will be created automatically
*.session        ← Will be created automatically
cookies.txt      ← Won't work on remote server
Procfile         ← Only for Railway/Heroku
render.yaml      ← Only for Render.com
runtime.txt      ← Only for Railway/Heroku/Render
```

---

## Keeping Bot Running (Free Account)

**The bot will STOP when you close the console.**

**Workaround (not recommended):**
1. Keep the browser tab open
2. Use `nohup` command:
```bash
nohup python3 main.py > bot.log 2>&1 &
```

**Problem:** This still stops after timeout or system maintenance.

---

## Better Alternative: Railway.app

**I strongly recommend using Railway.app instead:**

### Why Railway is Better:
- ✅ **100% Free** (500 hours/month)
- ✅ **Always-on** (24/7)
- ✅ **No browser needed**
- ✅ **Automatic restarts**
- ✅ **Better performance**

### How to Deploy to Railway:

1. Go to https://railway.app
2. Sign up with GitHub
3. Click **"New Project"**
4. Click **"Deploy from GitHub repo"**
5. Select your bot repository
6. Add environment variables:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
7. Click **"Deploy"**

**Done! Your bot runs 24/7 for free!**

---

## Troubleshooting PythonAnywhere

### "ModuleNotFoundError"
```bash
pip3 install --user -r requirements.txt
```

### "Permission denied"
```bash
chmod +x main.py
```

### Bot stops after closing browser
- This is expected on free tier
- Upgrade to paid account for always-on tasks
- OR use Railway.app (free and always-on)

### "CPU limit exceeded"
- Free accounts have 100 seconds/day CPU limit
- Your bot uses CPU when processing requests
- Upgrade to paid account for more CPU time

---

## My Recommendation

**Don't use PythonAnywhere for this bot.**

**Use Railway.app instead:**
1. Completely free
2. Always-on 24/7
3. No browser needed
4. Better performance
5. Easier deployment

I've already created the `Procfile` for you. Just:
1. Sign up on Railway.app
2. Deploy from GitHub or local folder
3. Add environment variables
4. Done!

See `DEPLOYMENT_GUIDE.md` for detailed Railway instructions.

---

## Summary

| Step | Action |
|------|--------|
| 1 | Sign up on PythonAnywhere |
| 2 | Open Bash console |
| 3 | Upload `main.py`, `requirements.txt`, `.env` |
| 4 | Run `pip3 install --user -r requirements.txt` |
| 5 | Run `python3 main.py` |
| 6 | Test your bot in Telegram |

**But remember:** Bot stops when you close browser on free tier!

**Better option:** Use Railway.app for free 24/7 hosting! 🚀
