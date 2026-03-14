import requests

from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("plot:"))
async def show_plot(callback: CallbackQuery):

    mal_id = callback.data.split(":")[1]

    r = requests.get(
        f"https://api.jikan.moe/v4/anime/{mal_id}"
    ).json()

    anime = r["data"]

    synopsis = anime["synopsis"]

    if not synopsis:
        synopsis = "Сюжет не найден."

    text = f"📖 Сюжет:\n\n{synopsis}"

    await callback.message.answer(text)

    await callback.answer()