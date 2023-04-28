from aiogram.fsm.state import State, StatesGroup

__all__ = ["MenuState"]


class MenuState(StatesGroup):
    BRIEF = State()
    ADVICE = State()
    HIKING = State()
    FIND = State()
