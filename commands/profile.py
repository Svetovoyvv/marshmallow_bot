from imports import *
from api import api

@dp.message_handler(commands=['/profile'])
async def cmd_profile(msg: Message):
    text = f'{markdown.bold("Профиль")}\n\nИстория заказов:\n'
    for i in api.order.get_all(client_id=api.client.get(chat_id=msg.chat.id).response.id).response:
        i = i[0]
        text += f'{i.product.name} ({i.count}) | {i.status_text}\n'
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Назад', callback_data='cancel_profile'))

    await msg.answer(
        text=text,
        reply_markup=kb
    )
