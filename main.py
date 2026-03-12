from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import TOKEN
from bot.handlers import register_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp)