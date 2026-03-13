from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎 Найти аниме"),
            KeyboardButton(text="🎲 Случайное")
        ],
        [
            KeyboardButton(text="🔥 Онгоинги"),
            KeyboardButton(text="🏆 Топ аниме")
        ],
        [
            KeyboardButton(text="❓ Помощь")
        ]
    ],
    resize_keyboard=True
)