from imports import *
from keyboards import keyboard_menu

@dp.message_handler(commands=['menu'])
async def cmd_menu(message: Message):
    await message.answer(
        'Привет! Выбери интересующее тебя действие!',
        reply_markup=keyboard_menu
    )
