from aiogram import Dispatcher
from aiogram.types import KeyboardButton, \
    ReplyKeyboardMarkup
from aiogram.types import Message 
from aiogram.dispatcher.filters import Text

async def welcome(message: Message):
    if message.from_user.id == "697153465":
        
        bots = ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("Бот с одной кнопкой"),
            KeyboardButton("Бот с 10 кнопками"),
        )
            
        await message.answer("Выберите бота: ", reply_markup=bots)

def register_welcome(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=["start"], state="*")
    dp.register_message_handler(welcome, Text(equals="Домой"), state="*")