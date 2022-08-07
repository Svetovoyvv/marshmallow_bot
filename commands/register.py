from imports import *
from api import api
from commands import cmd_menu
@dp.message_handler(content_types=['contact'])
async def cmd_contact(message: Message):
    r = api.client.get(chat_id=message.chat.id)
    if not r.status:
        return await message.answer('Произошла ошибка.')
    # print(r)
    if r.response is not None:
        await message.answer('Клиент уже зарегистрирован.')
        return cmd_menu(message)
    r = api.client.add(
        chat_id=message.chat.id,
        phone_number=message.contact.phone_number
    )
    if r.status:
        await message.answer(
            'Клиент зарегистрирован. Ваш номер: %s' % r.response,
        )
        await cmd_menu(message)
    else:
        await message.answer(r.err)
