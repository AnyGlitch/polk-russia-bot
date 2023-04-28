from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F, Router
from aiogram.enums import ParseMode

from source.keyboards import hiking_menu_keyboard
from source.messages import (
    hiking_menu_message,
    invite_info_message,
    pillar_info_message,
    taboo_info_message,
)
from source.routers.back import back_handler
from source.states import MenuState

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram.types import Message

__all__ = ["hiking_router"]

hiking_router = Router(name="Hiking Router")


@hiking_router.message(MenuState.BRIEF, F.text == "1")
async def hiking_menu_handler(message: Message, state: FSMContext) -> None:
    await message.answer(hiking_menu_message, reply_markup=hiking_menu_keyboard)
    await state.set_state(MenuState.HIKING)


@hiking_router.message(MenuState.HIKING, F.text == "2")
async def pillar_info_handler(message: Message) -> None:
    await message.answer(pillar_info_message, parse_mode=ParseMode.HTML)
    await back_handler(message)


@hiking_router.message(MenuState.HIKING, F.text == "3")
async def invite_info_handler(message: Message) -> None:
    await message.answer(invite_info_message)
    await back_handler(message)


@hiking_router.message(MenuState.HIKING, F.text == "4")
async def taboo_info_handler(message: Message) -> None:
    await message.answer(taboo_info_message)
    await back_handler(message)
