# handlers/command_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.logger import setup_logger

logger = setup_logger()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("مستندسازی لحظه‌ای", callback_data='instant')],
        [InlineKeyboardButton("مستندسازی دسته‌ای", callback_data='batch')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('لطفاً حالت مورد نظر خود را انتخاب کنید:', reply_markup=reply_markup)

async def document_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("مستندسازی لحظه‌ای", callback_data='instant')],
        [InlineKeyboardButton("مستندسازی دسته‌ای", callback_data='batch')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('لطفاً حالت مورد نظر خود را انتخاب کنید:', reply_markup=reply_markup)
