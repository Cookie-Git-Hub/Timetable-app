import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv
import os
# import time
# from functions.parsing import perform_parsing

load_dotenv()

# async def timer():
#     await perform_parsing()
#     print("parsing called")


async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    # for i in range(0,2):
    #     await timer()
    #     time.sleep(5)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

