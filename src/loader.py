from src.config import TELEGRAM_BOT_TOKEN

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

bot = Bot(TELEGRAM_BOT_TOKEN)
storage = RedisStorage2(db=8)
dp = Dispatcher(bot, storage=storage)
