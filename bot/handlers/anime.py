from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import requests

router = Router()


@router.message(Command("anime"))
async def search_anime(message: Message):

    query = message.text.replace("/anime", "").strip()

    if not query:
        await message.answer("Напиши название аниме\n\nПример:\n/anime Naruto")
        return

    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    r = requests.get(url).json()

    if not r["data"]:
        await message.answer("Аниме не найдено 😢")
        return

    anime = r["data"][0]

    title = anime["title"]
    score = anime["score"]
    episodes = anime["episodes"]
    synopsis = anime["synopsis"]
    image = anime["images"]["jpg"]["image_url"]

    text = (
        f"🎬 {title}\n\n"
        f"⭐ Рейтинг: {score}\n"
        f"📺 Эпизоды: {episodes}\n\n"
        f"{synopsis[:400]}..."
    )

    await message.answer_photo(image, caption=text)