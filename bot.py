from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
import config
import time
from eng_words_module import word_and_context
from autocheck_module import check_voting

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Available commands: /random /start_autocheck ')


@dp.message_handler(commands=['random'])
async def send_random_word_and_context(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context())

is_running = False

@dp.message_handler(commands=['start_autocheck'])
async def start_bitmart_vote_autocheck(message: types.Message):
    global is_running
    is_running = True

    chat_id = message.from_user.id
    old_voting = ""

    while is_running:
        current_voting = check_voting.get_current_voting()
        if current_voting != old_voting:
            await bot.send_message(chat_id=chat_id, text=f"NEW BITMART VOTING: {current_voting}")
            old_voting = current_voting
        else: 
            await bot.send_message(chat_id=chat_id, text=".")

        time.sleep(15)

@dp.message_handler(commands=['stop_autocheck'])
async def stop_bitmart_vote_authocheck(message: types.Message):

    global is_running
    is_running = False

    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="autocheck stopped")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
