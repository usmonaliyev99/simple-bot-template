from src.loader import dp

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

from src.bot.states.main_state import MainState


@dp.message_handler(commands=["start"], state="*")
async def start(message: Message, state: FSMContext):

    await MainState.phone_number.set()

    await message.answer(
        text="You are welcome!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("Send phone number", request_contact=True)]],
            resize_keyboard=True,
        ),
    )
