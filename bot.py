from aiogram import Bot, types, Dispatcher, executor
import asyncio
import config
import time
import random
from eng_words_module import word_and_context
from autocheck_module import check_voting, check_new_listings

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
old_voting = ""
old_listing = ""


async def bitmart_vote_autocheck(chat_id: int):
    global old_voting
    current_voting = check_voting.get_current_voting()
    print('still checking bitmart..')
    if current_voting != old_voting:
        old_voting = current_voting
        await bot.send_message(chat_id, f"NEW VOTING: {current_voting}")


async def bybit_listings_autocheck(chat_id: int):
    global old_listing
    current_listing = check_new_listings.get_current_listing()
    print('still checking bybit..')
    if current_listing != old_listing:
        old_listing = current_listing
        await bot.send_message(chat_id, f"NEW LISTING: {current_listing}")


@dp.message_handler(commands=['start_autocheck'])
async def start_autocheck(message: types.Message):
    chat_id = message.from_user.id
    global is_running
    if not is_running:
        is_running = True
        await bot.send_message(chat_id, '▶️ autocheck started ')
        while is_running == True:
            asyncio.create_task(bitmart_vote_autocheck(chat_id))
            asyncio.create_task(bybit_listings_autocheck(chat_id))
            await asyncio.sleep(random.randint(25, 50))
    else:
        await bot.send_message(chat_id=chat_id, text="▶️ autocheck is already running")


# /stop_autocheck

@dp.message_handler(commands=['stop_autocheck'])
async def stop_bitmart_vote_authocheck(message: types.Message):
    global is_running
    chat_id = message.from_user.id
    if is_running:
        print('stop autocheck.')
        is_running = False
        await bot.send_message(chat_id=chat_id, text="⏸ autocheck stopped")
    else:
        await bot.send_message(chat_id=chat_id, text="⏸ autocheck is not running now")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
