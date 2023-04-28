from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F, Router

from source.config import ADVICE_CHAT_ID
from source.keyboards import empty_keyboard
from source.messages import advice_message
from source.routers.back import back_handler
from source.states import MenuState

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram.types import Message, User

__all__ = ["advice_router"]

advice_router = Router(name="Advice Router")


@advice_router.message(MenuState.BRIEF, F.text == "3")
async def advise_handler(message: Message, state: FSMContext) -> None:
    await message.answer(advice_message, reply_markup=empty_keyboard)
    await state.set_state(MenuState.ADVICE)


@advice_router.message(MenuState.ADVICE, F.text.as_("issue"))
async def send_issue_handler(message: Message, state: FSMContext) -> None:
    forward = await message.forward(ADVICE_CHAT_ID)
    await message.pin()
    await forward.pin()
    await state.set_state(MenuState.BRIEF)
    await back_handler(message)


@advice_router.message(
    F.chat.id == ADVICE_CHAT_ID,
    F.reply_to_message.as_("to_message"),
    F.reply_to_message.forward_from.as_("to_user"),
)
async def send_answer_handler(
    message: Message,
    to_message: Message,
    to_user: User,
) -> None:
    forward = await message.forward(to_user.id)
    await to_message.unpin()
    await forward.pin()
