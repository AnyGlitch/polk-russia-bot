from aiogram import html

__all__ = ["find_hero_link", "find_hero_message"]

find_hero_link = "https://www.polkrf.ru/veteran/pomosh-v-poiske"

find_hero_message = (
    "Подробная инструкция о том, как найти информацию о ветеранах, "
    "размещена на сайте Бессмертного полка России "
    f"{html.link('по ссылке', find_hero_link)}:"
)
