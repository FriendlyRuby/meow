from aiogram import Router
from aiogram.types import CallbackQuery
import requests

from deep_translator import GoogleTranslator
from bot.handlers.anime import send_anime_card

router = Router()


@router.callback_query(lambda c: c.data.startswith("select_"))
async def select_anime(callback: CallbackQuery):

    mal_id = callback.data.split("_")[1]

    url = f"https://api.jikan.moe/v4/anime/{mal_id}"

    r = requests.get(url).json()

    anime = r["data"]

    await send_anime_card(callback.message, anime)

    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("story_"))
async def show_story(callback: CallbackQuery):

    mal_id = callback.data.split("_")[1]

    url = f"https://api.jikan.moe/v4/anime/{mal_id}"

    r = requests.get(url).json()

    anime = r["data"]

    synopsis = anime["synopsis"]

    try:
        synopsis_ru = GoogleTranslator(
            source="auto",
            target="ru"
        ).translate(synopsis)
    except:
        synopsis_ru = synopsis

    synopsis_ru = synopsis_ru.replace(
        "[Written by MAL Rewrite]", ""
    ).strip()

    synopsis_ru = synopsis_ru[:1500]

    await callback.message.answer(
        f"📖 Сюжет:\n\n{synopsis_ru}"
    )

    await callback.answer()