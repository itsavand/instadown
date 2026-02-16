# How to Set Up Cookies on Railway

Since Railway makes it hard to upload files like `cookies.txt`, you can now just **Copy & Paste** the cookie text into a variable.

## Step 1: Get the Cookie Text
1.  Use the **"Get cookies.txt LOCALLY"** extension (Chrome/Edge) or **"cookies.txt"** (Firefox).
2.  Log in to Instagram and export the cookies.
3.  Open the downloaded file with a text editor (Notepad, TextEdit, VS Code).
4.  **Select All** (Ctrl+A or Cmd+A) and **Copy** (Ctrl+C or Cmd+C).

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
