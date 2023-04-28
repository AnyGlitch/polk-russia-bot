from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

__all__ = ["get_numbered_keyboard"]


def get_numbered_keyboard(start: int, end: int) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text=str(num)) for num in range(start, end)],
        ],
    )
