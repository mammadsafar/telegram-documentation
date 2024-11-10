# services/audio_converter.py

from pydub import AudioSegment
import os

def convert_ogg_to_wav(ogg_path, wav_path):
    try:
        audio = AudioSegment.from_ogg(ogg_path)
        audio.export(wav_path, format="wav")
        return True
    except Exception as e:
        print(f"Error converting OGG to WAV: {e}")
        return False
