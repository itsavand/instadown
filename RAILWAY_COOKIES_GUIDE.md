# How to Set Up Cookies on Railway

Since Railway makes it hard to upload files like `cookies.txt`, you can now just **Copy & Paste** the cookie text into a variable.

## Step 0: Install the Extension
You need a specific browser extension to get the cookies.

### Option A: Google Chrome or Microsoft Edge
1.  **Click this link**: [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpcafejbcwbkm)
2.  Click the blue **"Add to Chrome"** button.
3.  Click **"Add extension"** in the pop-up.
4.  Look for the **Cookie Icon** 🍪 in your top-right toolbar.
    *   *If you don't see it, click the Puzzle Piece 🧩 icon and Pin it.*

### Option B: Firefox
1.  **Click this link**: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)
2.  Click **"Add to Firefox"**.
3.  Click **"Add"**.

## Step 1: Get the Cookie Text
1.  Go to [Instagram.com](https://www.instagram.com/) and log in.
2.  Click the **Cookie Icon** 🍪 you just installed.
3.  Click **"Export"** or **"Download"** (or sometimes "Copy content").
4.  Open the file it gives you with **Notepad** (Windows) or **TextEdit** (Mac).
5.  **Select All** the text and **Copy** it.

## Step 2: Add Variable to Railway
1.  Go to your **Railway Dashboard**.
2.  Click on your **Project**.
3.  Click on the **Variables** tab.
4.  Click **"New Variable"**.
5.  **VARIABLE NAME**: `COOKIES_CONTENT`
6.  **VALUE**: Paste the text you copied in Step 1.
7.  Click **Add**.

## Step 3: Redeploy
Railway usually redeploys automatically when you change variables.
If not, go to **Deployments** and click **Redeploy**.

The bot will now see the `COOKIES_CONTENT` variable, create the `cookies.txt` file for itself, and log "Found COOKIES_CONTENT env var".
