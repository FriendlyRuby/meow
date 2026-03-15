from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import requests

router = Router()


@router.message(Command("top"))
async def top_anime(message: Message):

    url = "https://api.jikan.moe/v4/top/anime"
    r = requests.get(url).json()

    text = "🏆 Топ аниме:\n\n"

    for anime in r["data"][:10]:

        title = anime["title"]
        score = anime["score"]

        text += f"⭐ {title} ({score})\n"

    await message.answer(text)