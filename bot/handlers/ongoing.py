from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.anime_api import get_ongoing

router = Router()


@router.message(Command("ongoing"))
async def ongoing(message: Message):

    anime_list = get_ongoing()

    text = "🔥 Онгоинги сезона:\n\n"

    for title, score, url in anime_list:
        text += f"⭐ {title} ({score})\n{url}\n\n"

    await message.answer(text)