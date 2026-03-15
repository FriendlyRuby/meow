from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "full_story")
async def full_story(callback: CallbackQuery):

    await callback.answer()

    await callback.message.answer(
        "📖 Полный сюжет уже выше ⬆️"
    )