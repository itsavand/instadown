# Deploying Instagram Downloader Bot to PythonAnywhere

## ⚠️ IMPORTANT WARNING

**PythonAnywhere is NOT recommended for Telegram bots** because:
- Free accounts have limited outbound internet access
- Long-running processes get killed
- No support for always-on bots on free tier

**Recommended alternatives:**
- **Railway.app** (easiest, free tier)
- **Render.com** (free tier)
- **Heroku** (free tier with credit card)
- **VPS** (DigitalOcean, Linode - $5/month)

---

## Option 1: Deploy to PythonAnywhere (Not Recommended)

### Step 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com
2. Sign up for a free account
3. Verify your email

### Step 2: Upload Files

**Files to upload:**
```
main.py
requirements.txt
.env
```

**DO NOT upload:**
- `.gitignore` (not needed)
- `README.md` (optional)
- `STORY_AUTH_GUIDE.md` (optional)
- `downloads/` folder (will be created automatically)
- `*.session` files (will be created automatically)

### Step 3: Upload via Web Interface

1. Go to **Files** tab
2. Create a new directory: `instagram_bot`
3. Upload these files:
   - `main.py`
   - `requirements.txt`
   - `.env`

### Step 4: Install Dependencies

1. Go to **Consoles** tab
2. Start a **Bash console**
3. Run these commands:

```bash
cd instagram_bot
pip3 install --user -r requirements.txt
```

### Step 5: Run the Bot

```bash
python3 main.py
```

**Problem:** The bot will stop when you close the browser or after timeout.

### Step 6: Keep Bot Running (Paid Account Only)

On paid accounts, you can use **Always-on tasks**, but this is NOT available on free tier.

---

## Option 2: Deploy to Railway.app (RECOMMENDED)

Railway is **perfect for Telegram bots** and has a generous free tier.

### Step 1: Prepare Your Files

Create a `Procfile` in your bot directory:

```
worker: python3 main.py
```

### Step 2: Create Railway Account

1. Go to https://railway.app
2. Sign up with GitHub
3. Create a new project

### Step 3: Deploy

1. Click **"Deploy from GitHub repo"**
2. OR click **"Deploy from local"**
3. Select your bot directory
4. Railway will auto-detect Python and install dependencies

### Step 4: Add Environment Variables

1. Go to **Variables** tab
2. Add these:
   - `API_ID` = your api_id
   - `API_HASH` = your api_hash
   - `BOT_TOKEN` = your bot token

### Step 5: Deploy

Railway will automatically:
- Install dependencies from `requirements.txt`
- Run your bot using the `Procfile`
- Keep it running 24/7

---

## Option 3: Deploy to Render.com (Also Recommended)

### Step 1: Create `render.yaml`

```yaml
services:
  - type: worker
    name: instagram-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: API_ID
        sync: false
      - key: API_HASH
        sync: false
      - key: BOT_TOKEN
        sync: false
```

### Step 2: Deploy

1. Go to https://render.com
2. Sign up with GitHub
3. Create new **Background Worker**
4. Connect your repository
5. Add environment variables
6. Deploy!

---

## Comparison Table

| Platform | Free Tier | Always-On | Easy Setup | Recommended |
|----------|-----------|-----------|------------|-------------|
| PythonAnywhere | ❌ Limited | ❌ No | ⚠️ Medium | ❌ No |
| Railway.app | ✅ Yes | ✅ Yes | ✅ Easy | ✅ **Best** |
| Render.com | ✅ Yes | ✅ Yes | ✅ Easy | ✅ Good |
| Heroku | ✅ Yes* | ✅ Yes | ⚠️ Medium | ✅ Good |
| VPS | ❌ $5/mo | ✅ Yes | ❌ Hard | ⚠️ Advanced |

*Requires credit card

---

## My Recommendation

**Use Railway.app** - it's the easiest and best for Telegram bots:

1. ✅ Free tier with 500 hours/month
2. ✅ Always-on bots
3. ✅ Easy deployment
4. ✅ Automatic restarts
5. ✅ No credit card required

---

## Files You Need to Upload (Any Platform)

### Required Files:
1. **`main.py`** - Your bot code
2. **`requirements.txt`** - Dependencies
3. **`.env`** OR environment variables in platform settings

### Optional Files:
4. **`Procfile`** (for Railway/Heroku)
5. **`render.yaml`** (for Render.com)

### DO NOT Upload:
- ❌ `.gitignore`
- ❌ `README.md`
- ❌ `*.session` files
- ❌ `downloads/` folder
- ❌ `cookies.txt` (won't work on remote server)

---

## Next Steps

**Tell me which platform you want to use:**
1. **Railway.app** (recommended) - I'll create the Procfile
2. **Render.com** - I'll create the render.yaml
3. **PythonAnywhere** (not recommended) - I'll give detailed steps
4. **VPS** - I'll create deployment script

Let me know and I'll prepare everything for you! 🚀
