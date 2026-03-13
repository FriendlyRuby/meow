from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "🎲 Случайное")
async def random_button(message: Message):

    from bot.handlers.random_anime import random_anime
    await random_anime(message)


@router.message(lambda message: message.text == "❓ Помощь")
async def help_button(message: Message):

    from bot.handlers.help import help_command
    await help_command(message)


@router.message(lambda message: message.text == "🔎 Найти аниме")
async def search_button(message: Message):

    await message.answer(
        "Напиши:\n\n"
        "/anime название\n\n"
        "Пример:\n"
        "/anime Naruto\n"
        "/anime ван пис"
    )


@router.message(lambda message: message.text == "🏆 Топ аниме")
async def top_button(message: Message):

    await message.answer(
        "Напиши команду:\n\n"
        "/top"
    )


@router.message(lambda message: message.text == "🔥 Онгоинги")
async def ongoing_button(message: Message):

    await message.answer(
        "Напиши команду:\n\n"
        "/ongoing"
    )