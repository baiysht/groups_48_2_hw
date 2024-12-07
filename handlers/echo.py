# echo.py
from aiogram import types, Dispatcher
from config import bot

async def echo_handler(message: types.Message):
    text = message.text
    if 'game' in message.text.lower():
        await message.answer_dice()
    elif text.isdigit():
        n = int(text)
        result = n ** 2
        await message.answer(result)
    else:
        await message.answer(message.text)


def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)