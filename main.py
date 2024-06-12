import logging
from aiogram import executor, types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.exceptions import NetworkError

API_TOKEN = "7459403561:AAFtZ9pFKfRXyvFmtIeMX7l5KbGEd_zxJ5Y"

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    waiting_for_button_click = State()


@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://vppnotcoin.netlify.app/")
    button1 = InlineKeyboardButton(text="Открыть веб-приложение", web_app=web_app_info)
    keyboard.add(button1)

    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>! Пожалуйста, нажмите кнопку, чтобы открыть веб-приложение.",
                         reply_markup=keyboard)
    await Form.waiting_for_button_click.set()

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except NetworkError as e:
        print(f"NetworkError occurred: {e}")
