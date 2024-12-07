# config.py
from aiogram import Bot, Dispatcher
from decouple import config


Admins = [1738351434, ]

token = config("TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)