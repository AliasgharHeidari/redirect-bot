"""
Simple Telegram redirect bot.

When a user starts the bot (or sends /start, or any message),
it replies with a button that opens your website.

This version also runs a tiny web server alongside the bot so it can
be deployed on Render's FREE "Web Service" tier. Render's free Web
Services need to respond to HTTP health-check pings; without this,
Render thinks the bot is unhealthy and starts a second instance,
which crashes the bot with a "Conflict" error from Telegram.

Setup:
1. pip install -r requirements.txt --break-system-packages
2. Set BOT_TOKEN as an environment variable (get it from @BotFather)
3. Start Command on Render: python bot.py
"""

import logging
import os
import threading

from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ==== CONFIG ====
BOT_TOKEN = os.environ.get("BOT_TOKEN", "PUT_YOUR_BOT_TOKEN_HERE")
WEBSITE_URL = "https://literallyme.ir"
BUTTON_TEXT = "🔗 Open Website"
MESSAGE_TEXT = "Tap below to visit my website:"
PORT = int(os.environ.get("PORT", 10000))  # Render sets PORT automatically
# ================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ---- tiny web server just to satisfy Render's health check ----
web_app = Flask(__name__)


@web_app.route("/")
def health():
    return "Bot is running."


def run_web_server():
    web_app.run(host="0.0.0.0", port=PORT)


# ---- telegram bot logic ----
async def send_redirect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(BUTTON_TEXT, url=WEBSITE_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(MESSAGE_TEXT, reply_markup=reply_markup)


def main():
    # Run the web server in a background thread so it doesn't block polling
    threading.Thread(target=run_web_server, daemon=True).start()

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", send_redirect))
    app.add_handler(MessageHandler(filters.ALL, send_redirect))

    print("Bot is running... press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
