from aiogram import Bot, Dispatcher
from environs import Env

env = Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")
CHAT_ID = env.str("CHAT_ID")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
