from aiogram import types
from services.anime_api import get_ongoing

def register_handlers(dp):

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.answer("Йо! Напиши /ongoing")

    @dp.message_handler(commands=['ongoing'])
    async def ongoing(message: types.Message):

        anime_list = get_ongoing()

        text = "🔥 Онгоинги:\n\n"

        for anime in anime_list:
            text += f"• {anime}\n"

        await message.answer(text)