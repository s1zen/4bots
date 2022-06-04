import os
import asyncio


from aiogram import Bot, Dispatcher, types

from dotenv import load_dotenv
from welcome import register_welcome
from one_btn import register_one_btn
from bot_ten_btns import register_bot_tens
from bot_support import register_bot_support


from aiogram.contrib.fsm_storage.memory import MemoryStorage

async def main():        
    load_dotenv("../.env")
    bot = Bot(token=os.getenv("admin_bot_token"))
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_welcome(dp)
    register_one_btn(dp)
    register_bot_tens(dp)
    register_bot_support(dp)
    print("Bot running!")
    
    await dp.start_polling()


if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        print("Bot stopped!")
    except Exception as e:
        print(f"Bot stopped!\nПроизошла ошибка: {e}")