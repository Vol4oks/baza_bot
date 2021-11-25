from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import message
from loader import dp
from pathlib import Path
import os
import subprocess

def du(path):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')

def list_users_dir(path):
    return os.listdir(path)

def user_path(message):
    return Path().joinpath("user_documents", f"{message.from_user.id}({message.from_user.full_name})")
    if os.path.exists(path):
        return path
    else:
        return None
    

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def downloader_document(message: types.Message):

    path_to_downloader = user_path(message)
    path_to_downloader.mkdir(parents=True, exist_ok=True)
    
    path_to_downloader = path_to_downloader.joinpath(message.document.file_name)
    try:
        await message.document.download(destination=path_to_downloader)
        await message.answer(f"Документ был сохранен")
    except Exception as ex:
        await message.answer(f"Документ не был сохранен")
        await message.answer(f"{ex}")


@dp.message_handler(text='/info')
async def show_dir(message: types.Message):
    path_to_downloader = user_path(message)
    if os.path.exists(path_to_downloader):
        dir_size = du(path_to_downloader)
        dir_list = list_users_dir(path_to_downloader)
        await message.answer(f"Размер папки {dir_size}")
        
        r_file = 'файлы: \n'
        r_dir = 'папки: \n'
        for i in dir_list:
            if '.' in i:
                r_file = r_file + i + '\n'
            else:
                r_dir = r_dir + i + '\n'
                
        await message.answer(f"{r_dir}")
        await message.answer(f"{r_file}")
    else:
        await message.answer("У вас нет папки")
    

@dp.message_handler(lambda message: message.text in list_users_dir(user_path(message)))
async def return_document(message):
    await message.answer(True)
    user_file = user_path(message).joinpath(message.text)
    await message.answer_document(open(user_file, 'rb'))

    
