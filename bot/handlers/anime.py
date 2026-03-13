from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

from deep_translator import GoogleTranslator

from bot.keyboards.anime_buttons import anime_keyboard
from bot.keyboards.anime_select import anime_select_keyboard
from bot.data.anime_synonyms import ANIME_SYNONYMS

router = Router()


@router.message(Command("anime"))
async def search_anime(message: Message):

    query = message.text.replace("/anime", "").strip().lower()

    if not query:
        await message.answer(
            "Напиши название аниме\n\nПример:\n/anime Naruto"
        )
        return

    # ---------- СЛОВАРЬ ----------

    if query in ANIME_SYNONYMS:
        query = ANIME_SYNONYMS[query]

    # ---------- ПЕРВЫЙ ПОИСК ----------

    url = f"https://api.jikan.moe/v4/anime?q={query}&type=tv&limit=5"
    r = requests.get(url).json()

    anime_list = r["data"]

    # ---------- ЕСЛИ НЕ НАШЛО ----------

    if not anime_list:

        try:
            query_en = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(query)

            url = f"https://api.jikan.moe/v4/anime?q={query_en}&type=tv&limit=5"
            r = requests.get(url).json()

            anime_list = r["data"]

        except:
            pass

    if not anime_list:
        await message.answer("Аниме не найдено 😢")
        return

    # ---------- ЕСЛИ НЕСКОЛЬКО ----------

    if len(anime_list) > 1:

        keyboard = anime_select_keyboard(anime_list)

        await message.answer(
            "Я нашёл несколько вариантов 👇",
            reply_markup=keyboard
        )

        return

    anime = anime_list[0]

    await send_anime_card(message, anime)


async def send_anime_card(message, anime):

    title = anime["title"]
    score = anime["score"] or "?"
    episodes = anime["episodes"] or "?"

    image = anime["images"]["jpg"]["image_url"]
    mal_url = anime["url"]
    mal_id = anime["mal_id"]

    # ---------- ГОД ----------

    year = anime["year"] if anime["year"] else "?"

    # ---------- ЖАНРЫ ----------

    genres = ", ".join([g["name"] for g in anime["genres"]])

    # ---------- ТРЕЙЛЕР ----------

    if anime["trailer"] and anime["trailer"]["url"]:
        trailer = anime["trailer"]["url"]
    else:
        title_for_search = title.replace(" ", "+")
        trailer = f"https://www.youtube.com/results?search_query={title_for_search}+trailer"

    keyboard = anime_keyboard(trailer, mal_url, mal_id)

    text = (
        f"🎬 <b>{title}</b>\n\n"
        f"⭐ Рейтинг: {score}\n"
        f"📺 Эпизоды: {episodes}\n"
        f"🎭 Жанры: {genres}\n"
        f"📅 Год: {year}"
    )

    await message.answer_photo(
        photo=image,
        caption=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )