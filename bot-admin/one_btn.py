import sqlite3

from aiogram import Dispatcher
from aiogram.types import KeyboardButton, \
    ReplyKeyboardMarkup
from aiogram.types import Message 
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class one_btn_edit(StatesGroup):
    btn_name = State()
    btn_link = State()
    description = State()


async def one_btn_change(message: Message):
    if message.from_user.id in [900793919, 697153465]:
        change_btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
            KeyboardButton("Название кнопки"),
            KeyboardButton("Ссылка кнопки"),
            KeyboardButton("Описание"),
            KeyboardButton("Домой")
        )
        
        await message.answer("Что изменить: ", reply_markup=change_btns)
    

async def change_name_btn(message: Message):
    if message.from_user.id in [900793919, 697153465]:
        await message.answer("Введите новое имя кнопки")
        await one_btn_edit.btn_name.set()
    
async def edit_name_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE botOneBtn SET name_btn = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
 
# ------------------------------------------------------------------- 

    
async def change_name_link(message: Message):
    if message.from_user.id in [900793919, 697153465]: 
        await message.answer("Введите новую ссылку кнопки (примечание: ссылка должна начинаться на https:// или http://)")
        await one_btn_edit.btn_link.set()

async def edit_name_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    
    try:    
        cursor_db.execute(f"UPDATE botOneBtn SET link_btn = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")

    connect_db.close()
    await state.finish()

# ------------------------------------------------------------------- 


async def change_description(message: Message):
    await message.answer("Введите новое описание")    
    await one_btn_edit.description.set()
    
async def edit_description(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor() 


    try:    
        cursor_db.execute(f"UPDATE botOneBtn SET description = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
def register_one_btn(dp: Dispatcher):
    dp.register_message_handler(one_btn_change, Text(equals="Бот с одной кнопкой"))
    
    dp.register_message_handler(change_name_btn, Text(equals="Название кнопки"))
    dp.register_message_handler(change_name_link, Text(equals="Ссылка кнопки"))
    dp.register_message_handler(change_description, Text(equals="Описание"))
    
    dp.register_message_handler(edit_name_btn, state=one_btn_edit.btn_name)
    dp.register_message_handler(edit_name_link, state=one_btn_edit.btn_link)
    dp.register_message_handler(edit_description, state=one_btn_edit.description)
    