from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):

    text = (
        "📖 *Помощь*\n\n"

        "🔎 `/anime название`\n"
        "Найти аниме\n\n"

        "🎲 `/random`\n"
        "Случайное аниме\n\n"

        "🔥 `/ongoing`\n"
        "Аниме которые выходят сейчас\n\n"

        "🏆 `/top`\n"
        "Топ аниме\n\n"

        "💡 Можно писать по-русски:\n"
        "`/anime ван пис`\n"
        "`/anime атака титанов`"
    )

    await message.answer(text, parse_mode="Markdown")