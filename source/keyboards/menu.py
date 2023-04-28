from source.keyboards.numbered import get_numbered_keyboard

__all__ = ["brief_menu_keyboard", "hiking_menu_keyboard"]

brief_menu_keyboard = get_numbered_keyboard(1, 4)
hiking_menu_keyboard = get_numbered_keyboard(1, 5)
