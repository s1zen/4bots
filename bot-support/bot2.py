import os
import sys
import asyncio


from aiogram import Bot, Dispatcher, types

from dotenv import load_dotenv
from check_db import main as check_db
from handlers import register_handlers

    
async def main():

    try:
        await check_db()
    except Exception as e:
        print(f"Ошибка в базах данных!\nОшибка: {e}")
        sys.exit()

    load_dotenv("../.env")
    bot = Bot(token=os.getenv("support_bot"))
    dp = Dispatcher(bot)
    
    register_handlers(dp)
    print("Bot running!")
    
    await dp.start_polling()
    
    
@dp.message_handler(content_types=["text"])
async def send_problem(message: types.Message):
    chat_id =  "-640603199"
    await message.forward(chat_id=chat_id, text=message.text)


if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        print("Bot stopped!")
    except Exception as e:
        print(f"Bot stopped!\nПроизошла ошибка: {e}")