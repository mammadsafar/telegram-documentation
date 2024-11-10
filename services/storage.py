# services/storage.py

from google.oauth2 import service_account
from googleapiclient.discovery import build
from utils.config import GOOGLE_DRIVE_API_KEY

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'client_secret_660512820472-kq084r589tbgoajtigq5hkpshtkrlcms.apps.googleusercontent.com.json'  # مسیر فایل کلید سرویس حساب

# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# drive_service = build('drive', 'v3', credentials=credentials)

def upload_to_google_drive(file_name, content):
    file_metadata = {
        'name': file_name,
        'mimeType': 'application/vnd.google-apps.document'
    }
    media = {
        'mimeType': 'text/plain',
        'body': content
    }
    # file = drive_service.files().create(
    #     body=file_metadata,
    #     media_body=media,
    #     fields='id'
    # ).execute()
    # return file.get('id')
    return 10