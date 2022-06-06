import os
import sqlite3
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from check_db import main as check_db

from pprint import pprint

load_dotenv("../.env")

bot = Bot(token=os.getenv("support_bot"))
dp = Dispatcher(bot)
chat_id =  -640603199


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if message.from_user.id == message.chat.id:
        connect_db = sqlite3.connect("../db/bots.db")
        cursor_db = connect_db.cursor()
        data_db = cursor_db.execute("SELECT * FROM bot_support WHERE id = ?", ("1")).fetchone()

        await bot.send_message(message.from_user.id, text=data_db[3], reply_markup={"inline_keyboard": [[{"text": data_db[1], "url": data_db[2]}]]})
        
        connect_db.close()
    
 
@dp.message_handler(content_types=['text'])
async def send_problem(message: types.Message):
    if message.from_user.id == message.chat.id:
        await message.forward(-1001712842771)
        await message.answer("Ваше обращение зарегистрировано.\nОжидайте ответа оператора.")
    elif message.chat.type == "supergroup":
        try:
            await bot.send_message(message["reply_to_message"]["forward_from"]["id"], f"Ответ от администратора: {message['text']}")
        except Exception:
            pass
        
async def main():
    try:
        await check_db()
    except Exception as e:
        print(f"Ошибка в базах данных!\nОшибка: {e}")
        sys.exit()
    
    print("Bot running!")
    
    await dp.start_polling()
    
    
if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        print("Bot stopped!")
    except Exception as e:
        print(f"Bot stopped!\nПроизошла ошибка: {e}")