#!/usr/bin/env python3
"""
Instagram Downloader Telegram Bot
Downloads Instagram videos, Reels, and Stories using Pyrogram and yt-dlp
"""

import os
import asyncio
import logging
from pathlib import Path
from typing import Optional

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
        'format': 'best',
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
        'nocheckcertificate': True,
        # Add user agent to avoid some blocks
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }
    
    # Add cookies file if it exists (for stories and private content)
    # Note: Browser cookie extraction doesn't work on remote servers
    if COOKIES_FILE.exists():
        options['cookiefile'] = str(COOKIES_FILE)
        logger.info(f"Using cookies file: {COOKIES_FILE}")
    else:
        logger.info("No cookies file found. Stories and private content will not be accessible.")
    
    return options


async def download_instagram_video(url: str) -> Optional[Path]:
    """
    Download Instagram video using yt-dlp
    
    Args:
        url: Instagram URL (post, reel, or story)
        
    Returns:
        Path to downloaded file or None if failed
    """
    # Generate unique filename based on timestamp
    timestamp = asyncio.get_event_loop().time()
    output_template = str(DOWNLOAD_DIR / f"instagram_{int(timestamp)}.%(ext)s")
    
    ydl_opts = get_yt_dlp_options(output_template)
    
    try:
        # Download in a thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(
            None,
            lambda: yt_dlp.YoutubeDL(ydl_opts).download([url])
        )
        
        # Find the downloaded file (yt-dlp adds extension automatically)
        downloaded_files = list(DOWNLOAD_DIR.glob(f"instagram_{int(timestamp)}.*"))
        
        if downloaded_files:
            return downloaded_files[0]
        else:
            logger.error("Download completed but file not found")
            return None
            
    except yt_dlp.utils.DownloadError as e:
        logger.error(f"yt-dlp download error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error during download: {e}")
        return None


async def cleanup_file(file_path: Path):
    """
    Delete file after sending
    
    Args:
        file_path: Path to file to delete
    """
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
        "📹 Send me an Instagram link and I'll download the video for you.\n\n"
        "**Supported content:**\n"
        "• Posts (videos)\n"
        "• Reels\n"
        "• Stories (requires authentication)\n\n"
        "**Just send me a link and I'll do the rest!**\n\n"
        "⚠️ Note: For private stories, make sure cookies.txt is configured."
    )
    await message.reply_text(welcome_text)


@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    """Handle /help command"""
    help_text = (
        "ℹ️ **How to use this bot:**\n\n"
        "1️⃣ Copy an Instagram link (post, reel, or story)\n"
        "2️⃣ Send it to me\n"
        "3️⃣ Wait while I download it\n"
        "4️⃣ Receive your video!\n\n"
        "**Supported formats:**\n"
        "• https://www.instagram.com/p/...\n"
        "• https://www.instagram.com/reel/...\n"
        "• https://www.instagram.com/stories/...\n\n"
        "**Limits:**\n"
        "• Maximum file size: 2GB\n"
        "• Private content requires cookies.txt configuration\n\n"
        "Need help? Contact the bot administrator."
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
    status_msg = await message.reply_text("⏳ Downloading your video... Please wait.")
    
    try:
        # Download the video
        file_path = await download_instagram_video(url)
        
        if not file_path:
            await status_msg.edit_text(
                "❌ **Download failed!**\n\n"
                "Possible reasons:\n"
                "• Invalid or expired link\n"
                "• Private content (requires cookies.txt)\n"
                "• Content unavailable\n"
                "• Rate limited by Instagram\n\n"
                "Please try again or contact support."
            )
            return
        
        # Check file size (Telegram limit with bot API is 50MB, with MTProto is 2GB)
        file_size = file_path.stat().st_size
        file_size_mb = file_size / (1024 * 1024)
        
        logger.info(f"File downloaded: {file_path.name} ({file_size_mb:.2f} MB)")
        
        if file_size > 2 * 1024 * 1024 * 1024:  # 2GB
            await status_msg.edit_text(
                f"❌ File is too large ({file_size_mb:.2f} MB).\n"
                "Maximum supported size is 2GB."
            )
            await cleanup_file(file_path)
            return
        
        # Update status
        await status_msg.edit_text(
            f"⬆️ Uploading video ({file_size_mb:.2f} MB)...\n"
            "This may take a while for large files."
        )
        
        # Send the video to user
        await message.reply_video(
            video=str(file_path),
            caption=f"✅ Downloaded from Instagram\n📦 Size: {file_size_mb:.2f} MB",
            supports_streaming=True
        )
        
        # Delete status message
        await status_msg.delete()
        
        # Clean up the downloaded file
        await cleanup_file(file_path)
        
        logger.info(f"Successfully processed request for user {message.from_user.id}")
        
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        await status_msg.edit_text(
            f"❌ **An error occurred:**\n`{str(e)}`\n\n"
            "Please try again or contact support."
        )


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
    logger.info(f"Download directory: {DOWNLOAD_DIR.absolute()}")
    logger.info(f"Cookies file: {'Found' if COOKIES_FILE.exists() else 'Not found'}")
    
    # Run the bot
    app.run()


if __name__ == "__main__":
    main()
