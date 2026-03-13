from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    text = (
        "🎌 Anime Helper Bot\n\n"
        "Я помогу найти аниме и узнать его сюжет.\n\n"

        "👇 Используй кнопки меню"
    )

    await message.answer(
        text,
        reply_markup=main_menu
    )