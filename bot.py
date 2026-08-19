"""
Simple Telegram redirect bot.

When a user starts the bot (or sends /start, or any message),
it replies with a button that opens your website.

Setup:
1. pip install python-telegram-bot --break-system-packages
2. Set your bot token below (get it from @BotFather)
3. Set your website URL below
4. Run: python3 bot.py
"""

import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ==== CONFIG ====
BOT_TOKEN = os.environ.get("BOT_TOKEN", "PUT_YOUR_BOT_TOKEN_HERE")
WEBSITE_URL = "https://literallyme.ir"
BUTTON_TEXT = "🔗 Open Website"
MESSAGE_TEXT = "Tap below to visit my website:"
# ================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def send_redirect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(BUTTON_TEXT, url=WEBSITE_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(MESSAGE_TEXT, reply_markup=reply_markup)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Respond to /start and to any other message the same way
    app.add_handler(CommandHandler("start", send_redirect))
    app.add_handler(MessageHandler(filters.ALL, send_redirect))

    print("Bot is running... press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
