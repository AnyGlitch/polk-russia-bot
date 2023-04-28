import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from source.config import GROUP_TOKEN, REDIS_URL
from source.database.engine import close_orm, init_orm
from source.routers import (
    advice_router,
    back_router,
    brief_router,
    find_router,
    hiking_router,
)

__all__ = ["main"]


async def main() -> None:
    bot = Bot(GROUP_TOKEN)

    storage = RedisStorage.from_url(REDIS_URL)

    dp = Dispatcher(storage=storage)

    dp.startup.register(init_orm)
    dp.shutdown.register(close_orm)

    dp.include_router(brief_router)

    brief_router.include_routers(back_router, hiking_router, advice_router)

    hiking_router.include_router(find_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
