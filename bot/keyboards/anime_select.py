from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_select_keyboard(anime_list):

    buttons = []

    for anime in anime_list:

        title = anime["title"]
        mal_id = anime["mal_id"]

        buttons.append([
            InlineKeyboardButton(
                text=title,
                callback_data=f"select_{mal_id}"
            )
        ])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard