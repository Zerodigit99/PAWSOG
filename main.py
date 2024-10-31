import asyncio
import logging
from contextlib import suppress
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Your bot's API token
API_TOKEN = "7712603902:AAHGFpU5lAQFuUUPYlM1jbu1u6XJGgs15Js"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define your command handlers
async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text("Hey! Welcome to Gray Zero Bot. This bot can help you automate tasks and manage multiple scripts.")

async def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the /help command is issued."""
    await update.message.reply_text("List of commands:\n/start - Welcome message\n/help - List of commands")

# Main function to set up and start the bot
async def main():
    logger.info("Starting the Telegram bot application...")
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Start the bot
    logger.info("Bot is polling...")
    await application.start()
    await application.updater.start_polling()

    # Keep the bot running until manually stopped
    await application.idle()
    await application.updater.stop()
    await application.stop()
    logger.info("Bot has stopped.")

if __name__ == '__main__':
    logger.info("Entering main block")
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
    logger.info("Application finished")