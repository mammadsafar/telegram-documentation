# utils/config.py

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GOOGLE_SPEECH_API_KEY = os.getenv('GOOGLE_SPEECH_API_KEY')
GPT_API_KEY = os.getenv('GPT_API_KEY')
GOOGLE_DRIVE_API_KEY = os.getenv('GOOGLE_DRIVE_API_KEY')
