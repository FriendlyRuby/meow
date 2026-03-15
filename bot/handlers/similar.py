from aiogram import Router
from aiogram.types import CallbackQuery
import requests

from bot.handlers.anime import send_anime_card

router = Router()


@router.callback_query(lambda c: c.data.startswith("similar_"))
async def similar_anime(callback: CallbackQuery):

    mal_id = callback.data.split("_")[1]

    url = f"https://api.jikan.moe/v4/anime/{mal_id}/recommendations"

    r = requests.get(url).json()

    data = r["data"][:5]

    await callback.message.answer("🔗 Похожие аниме:")

    for item in data:

        anime = item["entry"]

        # получаем полную инфу
        info = requests.get(
            f"https://api.jikan.moe/v4/anime/{anime['mal_id']}"
        ).json()["data"]

        await send_anime_card(callback.message, info)

    await callback.answer()