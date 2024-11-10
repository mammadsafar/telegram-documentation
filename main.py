# main.py

import asyncio
import sys

from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from handlers.command_handler import start, document_command
from handlers.voice import voice_handler
from handlers.callback_handler import button_callback
from utils.logger import setup_logger

logger = setup_logger()

def main():
    from utils.config import TELEGRAM_TOKEN
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # اضافه کردن هندلرها
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('document', document_command))
    app.add_handler(voice_handler)
    app.add_handler(CallbackQueryHandler(button_callback))

    logger.info("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
    # تنظیم سیاست حلقه رویداد برای ویندوز
    # if sys.platform.startswith('win'):
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # asyncio.run(main())
