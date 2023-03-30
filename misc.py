import logging
import os
from aiogram import Bot, Dispatcher
from game import Game


bot = Bot(token="6183110716:AAE5uKNdv7widhFjpdwPRxACc41Hiy1RHFo")
dp = Dispatcher(bot)
g = Game('crocobot.db')
logging.basicConfig(level=logging.INFO)
