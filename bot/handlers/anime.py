from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import requests

from deep_translator import GoogleTranslator
from bot.keyboards.anime_buttons import anime_keyboard

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
    mal_url = anime["url"]

    # трейлер
    trailer = anime["trailer"]["url"]

    # перевод
    try:
        synopsis_ru = GoogleTranslator(source="auto", target="ru").translate(synopsis)
    except:
        synopsis_ru = synopsis

    synopsis_ru = synopsis_ru[:1500]

    keyboard = anime_keyboard(trailer, mal_url)

    short_text = (
        f"🎬 {title}\n\n"
        f"⭐ Рейтинг: {score}\n"
        f"📺 Эпизоды: {episodes}"
    )

    await message.answer_photo(
        image,
        caption=short_text,
        reply_markup=keyboard
    )

    await message.answer(
        f"📖 Сюжет:\n\n{synopsis_ru}"
    )