from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

__all__ = ["choice_keyboard"]

choice_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="ДA"), KeyboardButton(text="HET")],
    ],
)
