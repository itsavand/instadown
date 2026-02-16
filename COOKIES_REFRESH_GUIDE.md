# How to Refresh Instagram Cookies

If the bot says **"Cookies Expired or Invalid"** or **"Content is unreachable"**, you need to update your `cookies.txt` file.

Instagram cookies expire after a few days or when you log out/change networks.

## Step 1: Get the Extension
You need a browser extension to export cookies in "Netscape" format.
*   **Chrome/Edge**: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpcafejbcwbkm)
*   **Firefox**: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

## Step 2: Export Cookies
1.  Open **Google Chrome** (or your browser) on your computer.
2.  Go to [Instagram.com](https://www.instagram.com/).
3.  **Log in** to the account you want the bot to use. 
    *   *Tip: Use a secondary account if possible, just in case.*
4.  Once logged in, click the **extension icon** (the cookie bite icon) in your browser toolbar.
5.  Click **"Export"** or **"Download"**.
6.  It will save a file like `instagram.com_cookies.txt`.

## Step 3: Update the Bot
1.  Rename the downloaded file to `cookies.txt`.
2.  **Replace** the old `cookies.txt` in your bot's folder with this new one.
3.  **Restart** the bot.

## Troubleshooting
*   **Still failing?** Try opening an Incognito window, logging into Instagram, and exporting cookies from there.
*   **2FA?** If your account has 2-factor authentication, `yt-dlp` might struggle. Try using a simple password-only account.
