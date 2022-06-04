import sqlite3

from aiogram import Dispatcher
from aiogram.types import KeyboardButton, \
    ReplyKeyboardMarkup
from aiogram.types import Message 
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class bot_support_edit(StatesGroup):
    btn_name_support = State()
    btn_link_support = State()
    description_support = State()
    
    
async def bot_support_change(message: Message):
    # if message.from_user.id == "697153465":
        change_btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
            KeyboardButton("Имя кнопки при старте"),
            KeyboardButton("Ссылку кнопки при старте"),
            KeyboardButton("Сообщение при старте"),
            KeyboardButton("Домой")
        )
        
        await message.answer("Что изменить: ", reply_markup=change_btns)
    

async def change_name_btn_support(message: Message):
    # if message.from_user.id == "697153465":
    await message.answer("Введите новое имя кнопки")
    await bot_support_edit.btn_name_support.set()
    
async def edit_name_btn_support(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_support SET name_btn = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
 
# ------------------------------------------------------------------- 

    
async def change_name_link_support(message: Message):
    # if message.from_user.id == "697153465": 
        await message.answer("Введите новую ссылку кнопки (примечание: ссылка должна начинаться на https:// или http://)")
        await bot_support_edit.btn_link_support.set()

async def edit_name_link_support(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    
    try:    
        cursor_db.execute(f"UPDATE bot_support SET link_btn = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")

    connect_db.close()
    await state.finish()

# ------------------------------------------------------------------- 


async def change_description_support(message: Message):
     # if message.from_user.id == "697153465": 
    await message.answer("Введите новое описание")    
    await bot_support_edit.description_support.set()
    
async def edit_description_support(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor() 


    try:    
        cursor_db.execute(f"UPDATE bot_support SET description = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
def register_bot_support(dp: Dispatcher):
    dp.register_message_handler(bot_support_change, Text(equals="Бот-поддержки"))
    
    dp.register_message_handler(change_name_btn_support, Text(equals="Имя кнопки при старте"))
    dp.register_message_handler(change_name_link_support, Text(equals="Ссылку кнопки при старте"))
    dp.register_message_handler(change_description_support, Text(equals="Сообщение при старте"))
    
    dp.register_message_handler(edit_name_btn_support, state=bot_support_edit.btn_name_support)
    dp.register_message_handler(edit_name_link_support, state=bot_support_edit.btn_link_support)
    dp.register_message_handler(edit_description_support, state=bot_support_edit.description_support)
    