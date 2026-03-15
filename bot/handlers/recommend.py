from aiogram import Router
from aiogram.types import Message, CallbackQuery

import requests

from bot.keyboards.genres import genres_keyboard
from bot.handlers.anime import send_anime_card

router = Router()


@router.message(lambda message: message.text == "🎯 Подобрать аниме")
async def recommend_menu(message: Message):

    await message.answer(
        "🎯 Выбери жанр:",
        reply_markup=genres_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("genre_"))
async def genre_selected(callback: CallbackQuery):

    genre_id = callback.data.split("_")[1]

    url = f"https://api.jikan.moe/v4/anime?genres={genre_id}&order_by=score&sort=desc&limit=5"

    r = requests.get(url).json()

    anime_list = r["data"]

    await callback.message.answer("🔥 Вот несколько рекомендаций:")

    for anime in anime_list:

        await send_anime_card(callback.message, anime)

    await callback.answer()