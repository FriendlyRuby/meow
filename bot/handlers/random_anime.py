from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import requests

from bot.handlers.anime import send_anime_card

router = Router()


@router.message(Command("random"))
async def random_anime(message: Message):

    url = "https://api.jikan.moe/v4/random/anime"

    r = requests.get(url).json()

    anime = r["data"]

    await send_anime_card(message, anime)