import sqlite3


from aiogram import Dispatcher
from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.types import Message 


async def welcome(message: Message):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    
    btn_1 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 1").fetchone()
    btn_2 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 2").fetchone()
    btn_3 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 3").fetchone()
    btn_4 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 4").fetchone()
    btn_5 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 5").fetchone()
    btn_6 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 6").fetchone()
    btn_7 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 7").fetchone()
    btn_8 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 8").fetchone()
    btn_9 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 9").fetchone()
    btn_10 = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 10").fetchone()
    
    description = cursor_db.execute("SELECT * FROM bot_ten_btns WHERE id = 11").fetchone()

    markup = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton(btn_1[1], btn_1[2]),
        InlineKeyboardButton(btn_2[1], btn_2[2]),
        InlineKeyboardButton(btn_3[1], btn_3[2]),
        InlineKeyboardButton(btn_4[1], btn_4[2]),
        InlineKeyboardButton(btn_5[1], btn_5[2]),
        InlineKeyboardButton(btn_6[1], btn_6[2]),
        InlineKeyboardButton(btn_7[1], btn_7[2]),
        InlineKeyboardButton(btn_8[1], btn_8[2]),
        InlineKeyboardButton(btn_9[1], btn_9[2]),
        InlineKeyboardButton(btn_10[1], btn_10[2])
        
        
    )
    # markup.row(
    #     InlineKeyboardButton(btn_1[1], btn_1[2]),
    #     InlineKeyboardButton(btn_2[1], btn_2[2]),
    #     InlineKeyboardButton(btn_3[1], btn_3[2])
    #     )
    # markup.row(
    #     InlineKeyboardButton(btn_4[1], btn_4[2]),
    #     InlineKeyboardButton(btn_5[1], btn_5[2])
    # )
    # markup.row(
    #     InlineKeyboardButton(btn_6[1], btn_6[2]),
    #     InlineKeyboardButton(btn_7[1], btn_7[2]),
    #     InlineKeyboardButton(btn_8[1], btn_8[2]),
    # )
    # markup.row(
    #     InlineKeyboardButton(btn_9[1], btn_9[2]),
    #     InlineKeyboardButton(btn_10[1], btn_10[2])
    # )
    


    await message.answer(text=description[3], reply_markup=markup)
    

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=["start"])