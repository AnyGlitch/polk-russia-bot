from aiogram import html

__all__ = [
    "find_hiking_message",
    "hiking_info_message",
    "not_find_hiking_link",
    "not_find_hiking_message",
]

hiking_info_message = (
    "Впишите в поле ответа регион Вашего проживания (название республики, "
    "края, области или автономного округа/области проживания)."
)

find_hiking_message = "{city} - {location} ({time})"

not_find_hiking_link = "https://www.polkrf.ru"

not_find_hiking_message = (
    "Информация о времени и месте проведения шествий в Вашем регионе "
    "уточняется, в скором времени она будет доступна здесь или на сайте "
    f"{html.link('Бессмертного полка России', not_find_hiking_link)}."
)
