from imports import *
from keyboards import keyboard_start
from api import api
from commands import cmd_menu
@dp.message_handler(commands=['start'])
async def cmd_start(msg: Message):
    r = api.client.get(chat_id=msg.chat.id)
    print(r)
    if r.response is not None:
        return await cmd_menu(msg)
    await msg.answer(
        '⚙ Для регистрации необходимо отправить номер телефона.',
        reply_markup=keyboard_start
    )

