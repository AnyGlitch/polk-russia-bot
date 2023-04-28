from aiogram import html

__all__ = ["back_link", "back_message", "not_back_message"]

back_link = "https://t.me/polk_russia"

back_message = "У Bас остались eщe вoпpocы?"

not_back_message = (
    f"{html.link('Подпишитесь', back_link)} "
    "на новости о шествии Бессмертного полка."
)
