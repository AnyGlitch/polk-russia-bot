from __future__ import annotations

from typing import TypeAlias

from source.database.models import HikingModel

__all__ = ["HikingService"]

MODEL: TypeAlias = HikingModel


class HikingService:
    @staticmethod
    async def get_or_none_by_city(city: str) -> MODEL | None:
        return await MODEL.get_or_none(city__iexact=city)
