import os

from requests import Session
from environs import Env

env = Env()
env.read_env()

ENV = env.str("ENV")

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")

WEBHOOK_HOST = env.str("WEBHOOK_HOST")
WEBHOOK_PATH = env.str("WEBHOOK_PATH")

WEBAPP_HOST = env.str("WEBAPP_HOST")
WEBAPP_PORT = env.int("WEBAPP_PORT")

api = Session()
api.auth = (env.str("BASIC_AUTH_USER"), env.str("BASIC_AUTH_PASSWORD"))
api.headers = {"Accept": "application/json", "Content-Type": "application/json"}
