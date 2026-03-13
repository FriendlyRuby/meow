import requests
import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.handlers.anime import send_anime_card

router = Router()


@router.message(Command("random"))
async def random_anime(message: Message):

    try:

        # случайная страница топа
        page = random.randint(1, 20)

        r = requests.get(
            f"https://api.jikan.moe/v4/top/anime?page={page}"
        ).json()

        anime_list = r["data"]

        # случайное аниме из топа
        anime_short = random.choice(anime_list)

        mal_id = anime_short["mal_id"]

        # получаем полную инфу
        anime = requests.get(
            f"https://api.jikan.moe/v4/anime/{mal_id}"
        ).json()["data"]

        await send_anime_card(message, anime)

    except Exception:
        await message.answer("😿 Ошибка получения аниме, попробуй ещё раз.")