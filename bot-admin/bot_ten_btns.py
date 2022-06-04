import sqlite3

from aiogram import Dispatcher
from aiogram.types import KeyboardButton, \
    ReplyKeyboardMarkup
from aiogram.types import Message 
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class bot_tens_edit(StatesGroup):
    btn_name_1 = State()
    btn_name_2 = State()
    btn_name_3 = State()
    btn_name_4 = State()
    btn_name_5 = State()
    btn_name_6 = State()
    btn_name_7 = State()
    btn_name_8 = State()
    btn_name_9 = State()
    btn_name_10 = State()
    
    btn_link_1 = State()
    btn_link_2 = State()
    btn_link_3 = State()
    btn_link_4 = State()
    btn_link_5 = State()
    btn_link_6 = State()
    btn_link_7 = State()
    btn_link_8 = State()
    btn_link_9 = State()
    btn_link_10 = State()
    
    description = State()


async def bot_tens_change(message: Message):
    if message.from_user.id == "697153465":
        change_btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
            KeyboardButton("Кнопки"),
            KeyboardButton("Общее описание"),
            KeyboardButton("Домой")
        )
        
        await message.answer("Что изменить: ", reply_markup=change_btns)
 
async def btns_change(message: Message):
    btns = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True).add(
        KeyboardButton("1 кнопка"),
        KeyboardButton("2 кнопка"),
        KeyboardButton("3 кнопка"),
        KeyboardButton("4 кнопка"),
        KeyboardButton("5 кнопка"),
        KeyboardButton("6 кнопка"),
        KeyboardButton("7 кнопка"),
        KeyboardButton("8 кнопка"),
        KeyboardButton("9 кнопка"),
        KeyboardButton("10 кнопка"),
        KeyboardButton("Домой")
    )
 
    await message.answer("Выберите кнопку", reply_markup=btns)

async def btn_change(message: Message, state: FSMContext):
    if message.from_user.id == "697153465":
        edit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
            KeyboardButton("Имя кнопки"),
            KeyboardButton("Ссылку кнопки"),
            KeyboardButton("Домой")
        )
        await message.answer(f"Выбрана кнопка: {message.text}\nЧто изменить: ", reply_markup=edit)
        await state.update_data(btn=message.text)

async def name_btn_change(message: Message, state: FSMContext):
    if message.from_user.id == "697153465":
        data = await state.get_data()
        try:
            if data["btn"] == "1 кнопка":
                await bot_tens_edit.btn_name_1.set()
            elif data["btn"] == "2 кнопка":
                await bot_tens_edit.btn_name_2.set()
            elif data["btn"] == "3 кнопка":
                await bot_tens_edit.btn_name_3.set()
            elif data["btn"] == "4 кнопка":
                await bot_tens_edit.btn_name_4.set()
            elif data["btn"] == "5 кнопка":
                await bot_tens_edit.btn_name_5.set()
            elif data["btn"] == "6 кнопка":
                await bot_tens_edit.btn_name_6.set()
            elif data["btn"] == "7 кнопка":
                await bot_tens_edit.btn_name_7.set()
            elif data["btn"] == "8 кнопка":
                await bot_tens_edit.btn_name_8.set()
            elif data["btn"] == "9 кнопка":
                await bot_tens_edit.btn_name_9.set()
            elif data["btn"] == "10 кнопка":
                await bot_tens_edit.btn_name_10.set()
            else:
                await message.answer("Что-то пошло не так.\nНажми кнопку: Домой")
            await message.answer("Введите новое имя кнопки")
        except Exception as e:
            btns = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True).add(
                KeyboardButton("1 кнопка"),
                KeyboardButton("2 кнопка"),
                KeyboardButton("3 кнопка"),
                KeyboardButton("4 кнопка"),
                KeyboardButton("5 кнопка"),
                KeyboardButton("6 кнопка"),
                KeyboardButton("7 кнопка"),
                KeyboardButton("8 кнопка"),
                KeyboardButton("9 кнопка"),
                KeyboardButton("10 кнопка"),
                KeyboardButton("Домой")
            )
            await message.answer("Выберите кнопку", reply_markup=btns)

async def link_btn_edit(message: Message, state: FSMContext):
    if message.from_user.id == "697153465":
    
        data = await state.get_data()
        try:
            if data["btn"] == "1 кнопка":
                await bot_tens_edit.btn_link_1.set()
            elif data["btn"] == "2 кнопка":
                await bot_tens_edit.btn_link_2.set()
            elif data["btn"] == "3 кнопка":
                await bot_tens_edit.btn_link_3.set()
            elif data["btn"] == "4 кнопка":
                await bot_tens_edit.btn_link_4.set()
            elif data["btn"] == "5 кнопка":
                await bot_tens_edit.btn_link_5.set()
            elif data["btn"] == "6 кнопка":
                await bot_tens_edit.btn_link_6.set()
            elif data["btn"] == "7 кнопка":
                await bot_tens_edit.btn_link_7.set()
            elif data["btn"] == "8 кнопка":
                await bot_tens_edit.btn_link_8.set()
            elif data["btn"] == "9 кнопка":
                await bot_tens_edit.btn_link_9.set()
            elif data["btn"] == "10 кнопка":
                await bot_tens_edit.btn_link_10.set()
            else:
                await message.answer("Что-то пошло не так.\nНажми кнопку: Домой")
            await message.answer("Введите новую ссылку кнопки (примечание: ссылка должна начинаться на https:// или http://)")
        except Exception as e:
            btns = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True).add(
                KeyboardButton("1 кнопка"),
                KeyboardButton("2 кнопка"),
                KeyboardButton("3 кнопка"),
                KeyboardButton("4 кнопка"),
                KeyboardButton("5 кнопка"),
                KeyboardButton("6 кнопка"),
                KeyboardButton("7 кнопка"),
                KeyboardButton("8 кнопка"),
                KeyboardButton("9 кнопка"),
                KeyboardButton("10 кнопка"),
                KeyboardButton("Домой")
            )
            await message.answer("Выберите кнопку", reply_markup=btns)  


# Edit name btn =========================
async def edit_1_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
    
async def edit_2_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 2")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
async def edit_3_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 3")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
async def edit_4_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 4")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
async def edit_5_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 5")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
async def edit_6_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 6")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()  
async def edit_7_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 7")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
async def edit_8_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 8")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
async def edit_9_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 9")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
async def edit_10_btn(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET name_btn = '{message.text}' WHERE id = 10")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
    
    # Edit link btn
async def edit_1_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 1")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
async def edit_2_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 2")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()

async def edit_3_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 3")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()

async def edit_4_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 4")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()

async def edit_5_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 5")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()

async def edit_6_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 6")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
async def edit_7_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 7")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
async def edit_8_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 8")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
async def edit_9_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 9")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()

async def edit_10_btn_link(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()


    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET link_btn = '{message.text}' WHERE id = 10")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
    
    

# ===========================================================================================
async def change_description(message: Message):
    await message.answer("Введите новое описание")    
    await bot_tens_edit.description.set()
    
 
async def edit_description(message: Message, state: FSMContext):
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor() 

    try:    
        cursor_db.execute(f"UPDATE bot_ten_btns SET description = '{message.text}' WHERE id = 11")
        connect_db.commit()
        await message.answer("Данные успешно изменены!")
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка!")
        
    connect_db.close()
    await state.finish()
    
    
def register_bot_tens(dp: Dispatcher):
    dp.register_message_handler(bot_tens_change, Text(equals="Бот с 10 кнопками"))
    dp.register_message_handler(btns_change, Text(equals="Кнопки"))
    dp.register_message_handler(btn_change, Text(endswith="кнопка"))
    dp.register_message_handler(name_btn_change, Text(equals="Имя кнопки"))
    dp.register_message_handler(link_btn_edit, Text(equals="Ссылку кнопки"))
    
    
    
    dp.register_message_handler(change_description, Text(equals="Общее описание"))
    dp.register_message_handler(edit_description, state=bot_tens_edit.description)
    
    
    # name edit
    dp.register_message_handler(edit_1_btn, state=bot_tens_edit.btn_name_1)
    dp.register_message_handler(edit_2_btn, state=bot_tens_edit.btn_name_2)
    dp.register_message_handler(edit_3_btn, state=bot_tens_edit.btn_name_3)
    dp.register_message_handler(edit_4_btn, state=bot_tens_edit.btn_name_4)
    dp.register_message_handler(edit_5_btn, state=bot_tens_edit.btn_name_5)
    dp.register_message_handler(edit_6_btn, state=bot_tens_edit.btn_name_6)
    dp.register_message_handler(edit_7_btn, state=bot_tens_edit.btn_name_7)
    dp.register_message_handler(edit_8_btn, state=bot_tens_edit.btn_name_8)
    dp.register_message_handler(edit_9_btn, state=bot_tens_edit.btn_name_9)
    dp.register_message_handler(edit_10_btn, state=bot_tens_edit.btn_name_10)
    
    # link edit
    dp.register_message_handler(edit_1_btn_link, state=bot_tens_edit.btn_link_1)
    dp.register_message_handler(edit_2_btn_link, state=bot_tens_edit.btn_link_2)
    dp.register_message_handler(edit_3_btn_link, state=bot_tens_edit.btn_link_3)
    dp.register_message_handler(edit_4_btn_link, state=bot_tens_edit.btn_link_4)
    dp.register_message_handler(edit_5_btn_link, state=bot_tens_edit.btn_link_5)
    dp.register_message_handler(edit_6_btn_link, state=bot_tens_edit.btn_link_6)
    dp.register_message_handler(edit_7_btn_link, state=bot_tens_edit.btn_link_7)
    dp.register_message_handler(edit_8_btn_link, state=bot_tens_edit.btn_link_8)
    dp.register_message_handler(edit_9_btn_link, state=bot_tens_edit.btn_link_9)
    dp.register_message_handler(edit_10_btn_link, state=bot_tens_edit.btn_link_10)