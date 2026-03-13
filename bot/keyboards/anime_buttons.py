from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_keyboard(trailer_url, mal_url, mal_id):

    buttons = []

    if trailer_url:
        buttons.append(
            [InlineKeyboardButton(text="🎬 Трейлер", url=trailer_url)]
        )

    buttons.append(
        [InlineKeyboardButton(text="⭐ Страница MAL", url=mal_url)]
    )

    buttons.append(
        [InlineKeyboardButton(
            text="📖 Полный сюжет",
            callback_data=f"story_{mal_id}"
        )]
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard