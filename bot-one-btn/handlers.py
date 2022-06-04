import sqlite3


from aiogram import Dispatcher
from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.types import Message 


async def welcome(message: Message):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    data_db = cursor_db.execute("SELECT * FROM botOneBtn WHERE id = ?", ("1")).fetchone()

    await message.answer(text=data_db[3], reply_markup={"inline_keyboard": [[{"text": data_db[1], "url": data_db[2]}]]})
    

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=["start"])