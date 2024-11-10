# handlers/voice_handler.py
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from telegram import Update
from telegram.ext import ContextTypes
import os
from services.speech_to_text import convert_speech_to_text
from services.documentation import organize_text
from services.storage import upload_to_google_drive
from utils.logger import setup_logger

logger = setup_logger()


# utils/message_utils.py
def split_message(text, limit=4000):
    """تقسیم متن به بخش‌های کوچکتر با طول حداکثر مشخص شده."""
    return [text[i:i+limit] for i in range(0, len(text), limit)]


async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        voice = update.message.voice
        file = await context.bot.get_file(voice.file_id)
        ogg_path = f"./downloads/{voice.file_id}.ogg"
        
        # دانلود فایل صوتی به فرمت OGG
        await file.download_to_drive(ogg_path)
        
        # تبدیل صوت به متن با استفاده از Whisper
        text = await convert_speech_to_text(ogg_path)
        # text = "این ویس را فقط دارم واسه تست میگیرم و اینکه میخوایم ببینیم یک سری کتاب داریم به چه صورت باید نگاهشون بکنیم؟ پولهایمان را چگونه دسته‌بندی بکنیم و در نهایت چه شکلی خروجی بدیم؟"
        
        # سازماندهی متن به مستندات
        # organized_text = await organize_text(text)
        organized_text = text
        
        # ذخیره مستندات در گوگل درایو
        doc_id = "ارسال لینک مستندات به کاربر"
        # doc_id = upload_to_google_drive(f"Document_{voice.file_id}.txt", organized_text)
        
        # ارسال لینک مستندات به کاربر
        # await update.message.reply_text(f"مستند شما با موفقیت ذخیره شد: https://docs.google.com/document/d/{doc_id}/edit")
        # ارسال متن به صورت بخش‌های کوچکتر
        messages = split_message(organized_text)
        print(messages)
        for msg in messages:
            await update.message.reply_text(msg)
        
        # حذف فایل OGG پس از پردازش
        if os.path.exists(ogg_path):
            os.remove(ogg_path)
        
    except Exception as e:
        logger.error(f"Error in handle_voice: {e}")
        await update.message.reply_text("خطایی در پردازش پیام صوتی رخ داده است.")


voice_handler = MessageHandler(filters.VOICE, handle_voice)