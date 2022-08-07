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
            """Привет! 
Данный бот предназначен для заказа кофе.

Воспользуйся следующими кнопками:
1. Сделать заказ 📱 - нажимай, если хочешь заказать чашечку крепкого или молочного кофе.
2. Активные заказы 🎟 - информация о заказах, которые в данный момент находятся в работе.
3. История заказов 📃 - информация о всех заказах.""",
        )
        await cmd_menu(message)
    else:
        await message.answer(r.err)
