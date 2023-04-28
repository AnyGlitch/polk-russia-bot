from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F, Router
from aiogram.enums import ParseMode

from source.database.services import HikingService
from source.keyboards import empty_keyboard
from source.messages import (
    find_hiking_message,
    hiking_info_message,
    not_find_hiking_message,
)
from source.routers.back import back_handler
from source.states import MenuState

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram.types import Message

__all__ = ["find_router"]

find_router = Router(name="Find Router")


@find_router.message(MenuState.HIKING, F.text == "1")
async def hiking_info_handler(message: Message, state: FSMContext) -> None:
    await message.answer(hiking_info_message, reply_markup=empty_keyboard)
    await state.set_state(MenuState.FIND)


@find_router.message(MenuState.FIND, F.text.as_("city"))
async def find_hiking_handler(message: Message, city: str) -> None:
    hiking = await HikingService.get_or_none_by_city(city)
    if hiking:
        text = find_hiking_message.format(
            city=hiking.city,
            location=hiking.location,
            time=hiking.time,
        )
    else:
        text = not_find_hiking_message
    await message.answer(text, parse_mode=ParseMode.HTML)
    await back_handler(message)
