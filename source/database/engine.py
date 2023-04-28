from tortoise import Tortoise, connections

from source.config import TORTOISE_ORM

__all__ = ["close_orm", "init_orm"]


async def init_orm() -> None:
    await Tortoise.init(TORTOISE_ORM)


async def close_orm() -> None:
    await connections.close_all()
