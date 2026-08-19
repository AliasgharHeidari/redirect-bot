# Telegram Redirect Bot

A tiny bot that replies with a button linking to your website.
Put the bot's `@username` in your Telegram bio — `@usernames` are
clickable in bios, unlike plain website URLs.

## Setup

1. **Create the bot**
   - Open Telegram, message [@BotFather](https://t.me/BotFather)
   - Send `/newbot`, pick a name and a username (must end in `bot`, e.g. `LiterallyMeBot`)
   - Copy the API token it gives you

2. **Configure**
   - Open `bot.py`
   - Replace `PUT_YOUR_BOT_TOKEN_HERE` with your token
   - Confirm `WEBSITE_URL` is set to `https://literallyme.ir`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

4. **Run it locally (optional test)**
   ```bash
   python3 bot.py
   ```
   Keep this running — if it stops, the bot won't reply.

5. **Deploy for free on Render (Web Service)**
   - Push these files to a GitHub repo
   - On [render.com](https://render.com), click **New +** → **Web Service**
   - Connect your repo
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - Under **Environment**, add a variable: `BOT_TOKEN` = your token from BotFather
   - Click **Create Web Service**

   This version includes a tiny built-in web server so Render's free
   Web Service health checks pass — without it, Render would think a
   polling-only bot is unhealthy and spin up a duplicate instance,
   causing a "Conflict" error from Telegram.

   Note: Render's free tier spins the service down after ~15 minutes
   of no HTTP traffic and takes a bit to wake back up. If you need it
   always instantly responsive, a paid tier or a platform like Railway
   avoids that cold start.

6. **Add to your Telegram bio**
   - Go to your bot's Telegram profile (search `@YourBotUsername`)
   - Copy that `@username`
   - Paste it into Settings → Edit Profile → Bio
   - It will render as a clickable link — tapping it opens the bot,
     which immediately shows the "Open Website" button

## How it works

Any message sent to the bot (including `/start`, which fires the
moment someone opens the bot from your bio) triggers a reply with
an inline button pointing straight at your site.
