from aiogram.dispatcher.filters.state import State, StatesGroup


class MainState(StatesGroup):
    phone_number = State()
    waiting = State()
    main = State()
