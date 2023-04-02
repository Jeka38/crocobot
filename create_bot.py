import logging
import os
from aiogram import Bot, Dispatcher
from game import Game
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
# bot = Bot(token="6084834897:AAFcxja55gKysFkEzjs3jMby80C2GhzWTzI")
dp = Dispatcher(bot)
g = Game('crocobot.db')
# logging.basicConfig(level=logging.INFO)