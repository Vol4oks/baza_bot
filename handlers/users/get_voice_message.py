from aiogram import types
from aiogram.types.message import Message
from loader import dp
from pathlib import Path
from vosk import KaldiRecognizer, Model
import subprocess

#async def parse_voice(model: Model, ph)

@dp.message_handler(content_types=[types.ContentType.VOICE])
async def wraite_voice(message: Message):
    voice = await message.voice.get_file()
    

