# Instagram Downloader Telegram Bot

A powerful Telegram bot built with Pyrogram and yt-dlp that downloads Instagram videos, Reels, and Stories. Supports files up to 2GB using MTProto.

## ✨ Features

- 📹 Download Instagram posts (videos)
- 🎬 Download Instagram Reels
- 📱 Download Instagram Stories (requires authentication)
- 🔐 Support for private content via cookies.txt
- 💾 Handles files up to 2GB (using MTProto)
- 🧹 Automatic cleanup of temporary files
- ⚡ Asynchronous processing
- 🛡️ Robust error handling

## 📋 Requirements

- Python 3.8 or higher
- Telegram API credentials (api_id and api_hash)
- Telegram Bot Token

## 🚀 Installation

### 1. Clone or download this project

```bash
cd "insta vid st down"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure credentials

#### Get Telegram API credentials:
1. Visit https://my.telegram.org
2. Log in with your phone number
3. Go to "API development tools"
4. Create an app to get your `api_id` and `api_hash`

#### Get Bot Token:
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the instructions
3. Copy your bot token

#### Create `.env` file:
```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```env
API_ID=12345678
API_HASH=your_api_hash_here
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 4. (Optional) Add cookies for private content

To download private stories or content from private accounts, you need to export your Instagram cookies:

#### Using browser extension (recommended):
1. Install a cookie export extension:
   - Chrome/Edge: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - Firefox: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)
2. Log into Instagram in your browser
3. Click the extension icon and export cookies for `instagram.com`
4. Save the file as `cookies.txt` in the bot directory

#### Manual method:
1. Log into Instagram in your browser
2. Open Developer Tools (F12)
3. Go to Application/Storage → Cookies → instagram.com
4. Export cookies in Netscape format
5. Save as `cookies.txt` in the bot directory

**Important:** The `cookies.txt` file should be in the same directory as `main.py`:
```
insta vid st down/
├── main.py
├── requirements.txt
├── .env
└── cookies.txt  ← Place it here
```

## 🎮 Usage

### Start the bot

```bash
python main.py
```

### Use the bot in Telegram

1. Start a chat with your bot in Telegram
2. Send `/start` to see the welcome message
3. Send any Instagram link (post, reel, or story)
4. Wait for the bot to download and send the video

### Supported URL formats:
- `https://www.instagram.com/p/ABC123/`
- `https://www.instagram.com/reel/ABC123/`
- `https://www.instagram.com/stories/username/123456789/`
- `https://instagr.am/p/ABC123/`

## 📁 Project Structure

```
insta vid st down/
├── main.py              # Main bot code
├── requirements.txt     # Python dependencies
├── .env                 # Configuration (create from .env.example)
├── .env.example         # Configuration template
├── cookies.txt          # Instagram cookies (optional, for private content)
├── downloads/           # Temporary download directory (auto-created)
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID from my.telegram.org | Yes |
| `API_HASH` | Telegram API Hash from my.telegram.org | Yes |
| `BOT_TOKEN` | Bot token from @BotFather | Yes |

### File Locations

- **Downloads**: Temporary files are stored in `downloads/` directory
- **Cookies**: Place `cookies.txt` in the root directory (same as `main.py`)
- **Session**: Pyrogram creates `instagram_bot.session` automatically

## ⚠️ Important Notes

### File Size Limits
- **With MTProto (api_id + api_hash)**: Up to 2GB ✅
- **Bot API only (just bot_token)**: Limited to 50MB ❌

This bot uses MTProto by configuring both api_id/api_hash AND bot_token, enabling the 2GB limit.

### Private Content
- Private stories and posts require valid Instagram cookies
- Cookies expire periodically - you'll need to re-export them
- The bot will inform you if cookies are needed but missing

### Rate Limiting
- Instagram may rate-limit requests
- If you encounter issues, wait a few minutes before trying again
- Consider using cookies to reduce rate limiting

## 🐛 Troubleshooting

### "Missing required environment variables"
- Make sure you created `.env` file from `.env.example`
- Verify all three variables are set correctly

### "Download failed - Private content"
- Export your Instagram cookies as `cookies.txt`
- Make sure cookies file is in Netscape format
- Ensure you're logged into Instagram when exporting

### "File is too large"
- The bot supports up to 2GB with proper MTProto configuration
- Verify you're using both api_id/api_hash and bot_token

### Bot doesn't respond
- Check if the bot is running (`python main.py`)
- Verify your bot token is correct
- Check the console for error messages

### Import errors
- Make sure you installed all dependencies: `pip install -r requirements.txt`
- Use Python 3.8 or higher

## 🔒 Security

- **Never share your `.env` file** - it contains sensitive credentials
- **Never commit cookies.txt** to version control
- Keep your bot token and API credentials private
- Regularly update your cookies for security

## 📝 License

This project is for educational purposes. Respect Instagram's Terms of Service and copyright laws.

## 🤝 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the console logs for error messages
3. Ensure all dependencies are installed correctly
4. Verify your credentials are correct

## 🔄 Updates

To update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

---

**Enjoy your Instagram Downloader Bot! 🎉**
