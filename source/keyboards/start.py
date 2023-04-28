from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

__all__ = ["start_keyboard"]

start_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Haчaть")],
    ],
)
