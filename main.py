import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import TOKEN
from bot.handlers.ongoing import router as ongoing_router
from bot.handlers.anime import router as anime_router
from bot.handlers.top import router as top_router
from bot.handlers.callbacks import router as callbacks_router
from bot.handlers.random_anime import router as random_router
from bot.handlers.start import router as start_router
from bot.handlers.help import router as help_router
from bot.handlers.menu import router as menu_router

async def main():

    bot = Bot(token=TOKEN)
    
    dp = Dispatcher()
    await bot.set_my_commands([
    BotCommand(command="anime", description="Найти аниме"),
    BotCommand(command="random", description="Случайное аниме"),
    BotCommand(command="ongoing", description="Онгоинги"),
    BotCommand(command="top", description="Топ аниме"),
    BotCommand(command="help", description="Помощь"),
]   )
    dp.include_router(ongoing_router)
    dp.include_router(anime_router)
    dp.include_router(top_router)
    dp.include_router(callbacks_router)
    dp.include_router(random_router)
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(menu_router)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())