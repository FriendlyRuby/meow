import requests

from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("trailer:"))
async def show_trailer(callback: CallbackQuery):

    mal_id = callback.data.split(":")[1]

    r = requests.get(
        f"https://api.jikan.moe/v4/anime/{mal_id}"
    ).json()

    anime = r["data"]

    trailer = anime["trailer"]["url"]

    if trailer:
        await callback.message.answer(f"🎬 Трейлер:\n{trailer}")
    else:
        await callback.message.answer("😿 Трейлер не найден.")

    await callback.answer()