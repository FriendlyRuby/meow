from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def genres_keyboard():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(text="⚔️ Битвы", callback_data="genre_1"),
                InlineKeyboardButton(text="❤️ Романтика", callback_data="genre_22")
            ],

            [
                InlineKeyboardButton(text="😂 Комедия", callback_data="genre_4"),
                InlineKeyboardButton(text="👻 Страшилка ужастик", callback_data="genre_14")
            ],

            [
                InlineKeyboardButton(text="🧠 Психология", callback_data="genre_40"),
                InlineKeyboardButton(text="⚽ Спорт", callback_data="genre_30")
            ]

        ]
    )

    return keyboard