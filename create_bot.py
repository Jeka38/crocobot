import logging
import os
from aiogram import Bot, Dispatcher
from game import Game
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)
datebase = Game('crocobot.db')