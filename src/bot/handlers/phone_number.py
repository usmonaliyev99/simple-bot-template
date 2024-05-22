from aiogram.types import (
    Message,
    ContentTypes,
    ReplyKeyboardRemove,
)
from aiogram.dispatcher import FSMContext

from src.loader import dp
from src.bot.states.main_state import MainState
from src.config import api


@dp.message_handler(content_types=ContentTypes.CONTACT, state=MainState.phone_number)
async def phone_number(message: Message, state: FSMContext):

    data = await state.get_data()

    phone_number = message.contact.phone_number.replace("+", "")

    data["phone_number"] = phone_number
    await state.set_data(data)

    await MainState.main.set()

    await message.answer(
        text=f"Your phone number is {phone_number}",
        reply_markup=ReplyKeyboardRemove(),
    )
