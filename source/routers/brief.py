from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, and_f, or_f

from source.keyboards import brief_menu_keyboard
from source.messages import brief_menu_message, find_hero_message
from source.routers.back import back_handler
from source.states import MenuState

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram.types import Message

__all__ = ["brief_router"]

brief_router = Router(name="Brief Router")


@brief_router.message(
    or_f(
        CommandStart(),
        F.text == "Haчaть",
        and_f(MenuState(), F.text == "ДA"),
    ),
)
async def brief_menu_handler(message: Message, state: FSMContext) -> None:
    await message.answer(brief_menu_message, reply_markup=brief_menu_keyboard)
    await state.set_state(MenuState.BRIEF)


@brief_router.message(MenuState.BRIEF, F.text == "2")
async def find_hero_handler(message: Message) -> None:
    await message.answer(find_hero_message, parse_mode=ParseMode.HTML)
    await back_handler(message)
