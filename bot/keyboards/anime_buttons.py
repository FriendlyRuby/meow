from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_keyboard(trailer, mal_url, mal_id):

     return InlineKeyboardMarkup(
        inline_keyboard=[
             [
                InlineKeyboardButton(
                    text="📖 Полный сюжет",
                    callback_data=f"story_{mal_id}"
                ),

                InlineKeyboardButton(
                    text="🎥 Трейлер",
                    url=trailer
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Похожие",
                    callback_data=f"similar_{mal_id}"
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