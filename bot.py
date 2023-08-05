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

# /start


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Available commands: /random_word /start_autocheck /stop_autocheck')

# /random word


@dp.message_handler(commands=['random_word'])
async def send_random_word_and_context(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context())

# /start_autocheck
is_running = False


@dp.message_handler(commands=['start_autocheck'])
async def start_autocheck(message: types.Message):
    global is_running
    chat_id = message.from_user.id
    if not is_running:
        is_running = True
        old_voting = ""

        while is_running:
            current_voting = check_voting.get_current_voting()
            if current_voting != old_voting:
                await bot.send_message(chat_id=chat_id, text=f"NEW VOTING: {current_voting}")
                old_voting = current_voting
            else:
                await bot.send_message(chat_id=chat_id, text=".")

            time.sleep(5)
    else:
        await bot.send_message(chat_id=chat_id, text="autocheck is already running")

# /stop_autocheck


@dp.message_handler(commands=['stop_autocheck'])
async def stop_bitmart_vote_authocheck(message: types.Message):
    global is_running
    chat_id = message.from_user.id
    if is_running:
        is_running = False
        await bot.send_message(chat_id=chat_id, text="autocheck stopped")
    else:
        await bot.send_message(chat_id=chat_id, text="autocheck is already stopped")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
