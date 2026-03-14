from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_keyboard(trailer, mal_url, mal_id):

     return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Сюжет",
                    callback_data=f"plot:{mal_id}"
                ),
                InlineKeyboardButton(
                    text="🎬 Трейлер",
                    callback_data=f"trailer:{mal_id}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Похожие",
                    callback_data=f"similar:{mal_id}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎲 Другое аниме",
                    callback_data="random"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌐 MAL",
                    url=f"https://myanimelist.net/anime/{mal_id}"
                )
            ]
        ]
    )