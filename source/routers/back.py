from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F, Router
from aiogram.enums import ParseMode

from source.keyboards import choice_keyboard, start_keyboard
from source.messages import back_message, not_back_message
from source.states import MenuState

if TYPE_CHECKING:
    from aiogram.types import Message

__all__ = ["back_handler", "back_router"]

back_router = Router(name="Back Router")


async def back_handler(message: Message) -> None:
    await message.answer(back_message, reply_markup=choice_keyboard)


@back_router.message(MenuState(), F.text == "HET")
async def not_back_handler(message: Message) -> None:
    await message.answer(
        not_back_message,
        parse_mode=ParseMode.HTML,
        reply_markup=start_keyboard,
    )
