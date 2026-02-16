#!/usr/bin/env python3
"""
Instagram Downloader Telegram Bot
Downloads Instagram videos, Reels, and Stories using Pyrogram and yt-dlp
"""

import os
import asyncio
import logging
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
import yt_dlp

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration from environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Validate configuration
if not all([API_ID, API_HASH, BOT_TOKEN]):
    raise ValueError("Missing required environment variables: API_ID, API_HASH, BOT_TOKEN")

# Create temporary download directory
DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

# Cookies file path (optional, for private content)
COOKIES_FILE = Path("cookies.txt")

# Initialize Pyrogram client
app = Client(
    "instagram_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


def get_yt_dlp_options(output_path: str) -> dict:
    """
    Configure yt-dlp options for Instagram downloads
    
    Args:
        output_path: Path where the file should be saved
        
    Returns:
        Dictionary of yt-dlp options
    """
    options = {
        'outtmpl': output_path,
        # 'format': 'best', # Commented out to allow images/mixed content
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
        'nocheckcertificate': True,
        'ignoreerrors': True, # Continue even if one file fails
        'skip_download': False,
        # Ensure we download thumbnails (often how images are served for some types)
        'writethumbnail': True,
        # Trust me, some images are only grabbed this way in yt-dlp for insta
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': 'https://www.instagram.com/',
    }
    
    # Add cookies file if it exists (for stories and private content)
    # Note: Browser cookie extraction doesn't work on remote servers
    if COOKIES_FILE.exists():
        options['cookiefile'] = str(COOKIES_FILE)
        logger.info(f"Using cookies file: {COOKIES_FILE}")
    else:
        logger.info("No cookies file found. Stories and private content will not be accessible.")
    
    return options


async def download_instagram_video(url: str) -> List[Path]:
    """
    Download Instagram content using yt-dlp.
    Supports posts, reels, stories, and carousels (multiple items).
    
    Args:
        url: Instagram URL
        
    Returns:
        List of paths to downloaded files
    
    Raises:
        Exception: If download fails or no files are found
    """
    # Generate unique timestamp for this download batch
    timestamp = str(int(asyncio.get_event_loop().time()))
    
    # Use %(id)s to ensure unique filenames for carousels/multiple items
    output_template = str(DOWNLOAD_DIR / f"instagram_{timestamp}_%(id)s.%(ext)s")
    
    ydl_opts = get_yt_dlp_options(output_template)
    
    try:
        # Download in a thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(
            None,
            lambda: yt_dlp.YoutubeDL(ydl_opts).download([url])
        )
        
        # Find all downloaded files matching this timestamp
        # We use glob to find files starting with the timestamp prefix
        downloaded_files = list(DOWNLOAD_DIR.glob(f"instagram_{timestamp}_*"))
        
        # Filter out `.part` files if any exist (incomplete downloads)
        downloaded_files = [f for f in downloaded_files if f.suffix != '.part']
        
        if downloaded_files:
            return downloaded_files
        else:
            raise Exception("Download completed but no files were found")
            
    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        logger.error(f"yt-dlp download error: {error_msg}")
        
        if "unreachable" in error_msg.lower() or "login" in error_msg.lower() or "sign in" in error_msg.lower():
            raise Exception("⚠️ **Cookies Expired or Invalid**\n\nPlease update your `cookies.txt` file.\nSee COOKIES_REFRESH_GUIDE.md for instructions.")
        elif "video unavailable" in error_msg.lower():
             raise Exception("⚠️ **Content Unavailable**\n\nThe story/video might have been deleted or is private.")
        else:
            raise Exception(f"Download error: {error_msg}")
            
    except Exception as e:
        logger.error(f"Unexpected error during download: {e}")
        raise e


async def cleanup_files(file_paths: List[Path]):
    """
    Delete files after sending
    
    Args:
        file_paths: List of paths to files to delete
    """
    for file_path in file_paths:
        try:
            if file_path.exists():
                file_path.unlink()
                logger.info(f"Deleted file: {file_path}")
        except Exception as e:
            logger.error(f"Error deleting file {file_path}: {e}")


def is_instagram_url(text: str) -> bool:
    """
    Check if text contains an Instagram URL
    
    Args:
        text: Text to check
        
    Returns:
        True if text contains Instagram URL
    """
    instagram_domains = [
        'instagram.com',
        'www.instagram.com',
        'instagr.am',
        'www.instagr.am'
    ]
    
    return any(domain in text.lower() for domain in instagram_domains)


@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    welcome_text = (
        "👋 **Welcome to Instagram Downloader Bot!**\n\n"
        "📹 Send me an Instagram link and I'll download it for you.\n\n"
        "**Supported content:**\n"
        "• Posts (videos & photos)\n"
        "• Reels\n"
        "• Stories (requires cookies)\n"
        "• Carousels (multiple items)\n\n"
        "**Just send me a link!**\n\n"
        "⚠️ Note: For private stories, set `COOKIES_CONTENT` env var."
    )
    await message.reply_text(welcome_text)


@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    """Handle /help command"""
    help_text = (
        "ℹ️ **How to use this bot:**\n\n"
        "1️⃣ Copy an Instagram link (post, reel, or story)\n"
        "2️⃣ Send it to me\n"
        "3️⃣ Receive your media!\n\n"
        "**Supported formats:**\n"
        "• https://www.instagram.com/p/...\n"
        "• https://www.instagram.com/reel/...\n"
        "• https://www.instagram.com/stories/...\n\n"
        "**Setup:**\n"
        "If stories fail, see RAILWAY_COOKIES_GUIDE.md to setup cookies."
    )
    await message.reply_text(help_text)


@app.on_message(filters.text & filters.private)
async def handle_message(client: Client, message: Message):
    """
    Handle incoming messages containing Instagram links
    
    Args:
        client: Pyrogram client
        message: Incoming message
    """
    text = message.text
    
    # Check if message contains an Instagram URL
    if not is_instagram_url(text):
        await message.reply_text(
            "❌ Please send me a valid Instagram link.\n"
            "Use /help to see supported formats."
        )
        return
    
    # Extract URL from text (simple approach - take the first word that looks like URL)
    words = text.split()
    url = None
    for word in words:
        if 'instagram.com' in word.lower() or 'instagr.am' in word.lower():
            url = word
            break
    
    if not url:
        await message.reply_text("❌ Could not find Instagram URL in your message.")
        return
    
    # Send processing message
    status_msg = await message.reply_text("⏳ Downloading content... Please wait.")
    
    downloaded_files = []
    
    try:
        # Download the content (returns a list of paths)
        downloaded_files = await download_instagram_video(url)
        
        # Calculate total size
        total_size = sum(f.stat().st_size for f in downloaded_files)
        total_size_mb = total_size / (1024 * 1024)
        
        # Check total size limit (2GB)
        if total_size > 2 * 1024 * 1024 * 1024:
            await status_msg.edit_text(
                f"❌ Total content size is too large ({total_size_mb:.2f} MB).\n"
                "Maximum supported total size is 2GB."
            )
            await cleanup_files(downloaded_files)
            return
        
        # Update status
        await status_msg.edit_text(
            f"⬆️ Uploading {len(downloaded_files)} item(s) ({total_size_mb:.2f} MB)..."
        )
        
        # Send each file
        for i, file_path in enumerate(downloaded_files):
            file_size_mb = file_path.stat().st_size / (1024 * 1024)
            extension = file_path.suffix.lower()
            caption = f"✅ Item {i+1}/{len(downloaded_files)} | 📦 {file_size_mb:.2f} MB"
            
            try:
                if extension in ['.jpg', '.jpeg', '.png', '.webp']:
                    await message.reply_photo(
                        photo=str(file_path),
                        caption=caption
                    )
                elif extension in ['.mp4', '.mov', '.avi', '.mkv']:
                    await message.reply_video(
                        video=str(file_path),
                        caption=caption,
                        supports_streaming=True
                    )
                else:
                    await message.reply_document(
                        document=str(file_path),
                        caption=caption
                    )
            except Exception as send_e:
                logger.error(f"Error sending file {file_path}: {send_e}")
                await message.reply_text(f"❌ Failed to send item {i+1}: {file_path.name}")
        
        # Delete status message
        await status_msg.delete()
        
        # Clean up the downloaded files
        await cleanup_files(downloaded_files)
        
        logger.info(f"Successfully processed request for user {message.from_user.id}: {len(downloaded_files)} files processed.")
            
    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        logger.error(f"yt-dlp download error: {error_msg}")
        
        # Check for authentication errors
        if "unreachable" in error_msg.lower() or "login" in error_msg.lower() or "sign in" in error_msg.lower():
            await status_msg.edit_text(
                "⚠️ **Cookies Expired or Invalid**\n\n"
                "Please update your `COOKIES_CONTENT` variable in Railway.\n"
                "See `RAILWAY_COOKIES_GUIDE.md` for instructions."
            )
        elif "video unavailable" in error_msg.lower():
             await status_msg.edit_text("⚠️ **Content Unavailable**\n\nThe story/video might have been deleted or is private.")
        else:
            await status_msg.edit_text(f"❌ **Download Error:**\n`{error_msg[:100]}...`") # limit error length
            
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        await status_msg.edit_text(
            f"❌ **An error occurred:**\n`{str(e)}`\n\n"
            "Please try again or contact support."
        )
        # Ensure cleanup on error
        if downloaded_files:
            await cleanup_files(downloaded_files)


@app.on_message(filters.video | filters.document)
async def handle_media(client: Client, message: Message):
    """Handle users sending media (inform them how to use the bot)"""
    await message.reply_text(
        "ℹ️ I can't process videos directly.\n"
        "Please send me an Instagram link instead!\n\n"
        "Use /help to see how to use this bot."
    )


def main():
    """Main entry point"""
    logger.info("Starting Instagram Downloader Bot...")

    # Check for COOKIES_CONTENT environment variable (for Railway/Render support)
    cookies_content = os.getenv("COOKIES_CONTENT")
    if cookies_content:
        logger.info("Found COOKIES_CONTENT env var, writing to cookies.txt")
        try:
            with open("cookies.txt", "w") as f:
                f.write(cookies_content)
        except Exception as e:
            logger.error(f"Failed to write cookies.txt from env var: {e}")

    logger.info(f"Download directory: {DOWNLOAD_DIR.absolute()}")
    logger.info(f"Cookies file: {'Found' if COOKIES_FILE.exists() else 'Not found'}")
    
    # Run the bot
    app.run()


if __name__ == "__main__":
    main()
