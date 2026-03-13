from aiogram import Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import requests

from bot.handlers.anime import send_anime_card

router = Router()


def genre_top_keyboard():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(text="⚔️ Action", callback_data="topgenre_1"),
                InlineKeyboardButton(text="❤️ Romance", callback_data="topgenre_22")
            ],

            [
                InlineKeyboardButton(text="😂 Comedy", callback_data="topgenre_4"),
                InlineKeyboardButton(text="👻 Horror", callback_data="topgenre_14")
            ],

            [
                InlineKeyboardButton(text="⚽ Sports", callback_data="topgenre_30")
            ]

        ]
    )

    return keyboard


@router.message(lambda message: message.text == "/topgenre")
async def top_genre(message: Message):

    await message.answer(
        "🏆 Выбери жанр для топа:",
        reply_markup=genre_top_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("topgenre_"))
async def genre_top(callback: CallbackQuery):

    genre_id = callback.data.split("_")[1]

    url = f"https://api.jikan.moe/v4/anime?genres={genre_id}&order_by=score&sort=desc&limit=5"

    r = requests.get(url).json()

    anime_list = r["data"]

    await callback.message.answer("🏆 Топ аниме этого жанра:")

    for anime in anime_list:

        await send_anime_card(callback.message, anime)

    await callback.answer()