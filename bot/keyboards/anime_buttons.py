from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_keyboard(trailer_url, mal_url):

    buttons = []

    if trailer_url:
        buttons.append(
            [InlineKeyboardButton(text="🎬 Трейлер", url=trailer_url)]
        )

    buttons.append(
        [InlineKeyboardButton(text="⭐ Страница MAL", url=mal_url)]
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard