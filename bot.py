from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
import config

bot = Bot(token=config.token)
dp = Dispatcher(bot)

#TODO Bot commands, bot logic modules

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
