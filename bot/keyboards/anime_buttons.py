from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_keyboard(trailer, mal_url, mal_id):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📖 Сюжет",
                    callback_data=f"plot_{mal_id}"
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
                    text="🌐 MAL",
                    url=mal_url
                )
            ]

        ]
    )

    return keyboard