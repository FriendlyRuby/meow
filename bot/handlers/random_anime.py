import requests
import random

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from bot.handlers.anime import send_anime_card
from bot.services.cache import get, set

router = Router()


def get_random_top_anime():

    # случайная страница топа
    page = random.randint(1, 20)

    r = requests.get(
        f"https://api.jikan.moe/v4/top/anime?page={page}"
    ).json()

    anime_list = r["data"]

    anime_short = random.choice(anime_list)

    mal_id = anime_short["mal_id"]

    cache_key = f"anime:{mal_id}"

    anime = get(cache_key)

    if not anime:

        anime = requests.get(
            f"https://api.jikan.moe/v4/anime/{mal_id}"
        ).json()["data"]

        set(cache_key, anime)

    return anime


@router.message(Command("random"))
async def random_anime(message: Message):

    try:

        anime = get_random_top_anime()

        await send_anime_card(message, anime)

    except Exception:

        await message.answer("😿 Ошибка получения аниме, попробуй ещё раз.")


@router.callback_query(F.data == "random")
async def random_again(callback: CallbackQuery):

    await callback.answer()

    try:

        anime = get_random_top_anime()

        await send_anime_card(callback.message, anime)

    except Exception:

        await callback.message.answer("😿 Ошибка получения аниме.")