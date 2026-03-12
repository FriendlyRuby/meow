import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from bot.handlers.ongoing import router as ongoing_router
from bot.handlers.anime import router as anime_router
from bot.handlers.top import router as top_router


async def main():

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(ongoing_router)
    dp.include_router(anime_router)
    dp.include_router(top_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())