from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import users
from loader import dp


#users = []

@dp.message_handler(lambda message: message.from_user.id not in users )
async def login(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer(f'К сожалению у тебя нет доступа к боту...')

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
