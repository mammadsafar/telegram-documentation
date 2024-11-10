# handlers/callback_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import setup_logger

logger = setup_logger()

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'instant':
        await query.edit_message_text(text="حالت مستندسازی لحظه‌ای فعال شد.")
        # فعال‌سازی منطق مستندسازی لحظه‌ای
    elif query.data == 'batch':
        await query.edit_message_text(text="حالت مستندسازی دسته‌ای فعال شد.")
        # فعال‌سازی منطق مستندسازی دسته‌ای
