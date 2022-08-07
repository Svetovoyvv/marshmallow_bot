from imports import *
from api import api
@dp.message_handler(commands=['active_orders'])
async def cmd_active_orders(msg: Message):
    a = api.order.get_active(client_id=api.client.get(chat_id=msg.chat.id).response.id)
    kb = InlineKeyboardMarkup()
    for i in a.response:
        if i[0].status not in [1, 2]:
            continue
        i = i[0]
        kb.add(InlineKeyboardButton(text=f'{i.product.name} ({i.count}) | {i.status_text}', callback_data='order_id_' + str(i.id)))
    kb.add(InlineKeyboardButton(text='Назад', callback_data='cancel_profile'))
    await msg.answer('Активные заказы', reply_markup=kb)

@dp.callback_query_handler(text_startswith='list_active_')
async def callback_list_active_orders(callback_query: CallbackQuery):
    a = api.order.get_active(client_id=api.client.get(chat_id=callback_query.message.chat.id).response.id)
    kb = InlineKeyboardMarkup()
    for i in a.response:
        if i[0].status not in [1, 2]:
            continue
        i = i[0]
        kb.add(InlineKeyboardButton(text=f'{i.product.name} ({i.count}) | {i.status_text}',
                                    callback_data='order_id_' + str(i.id)))
    kb.add(InlineKeyboardButton(text='Назад', callback_data='cancel_profile'))
    await callback_query.message.edit_text('Активные заказы', reply_markup=kb)
@dp.callback_query_handler(text_startswith='order_id_')
async def callback_active_orders(callback_query: CallbackQuery):
    order_id = int(callback_query.data.split('_')[-1])
    a = api.order.get(order_id=order_id).response
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Назад', callback_data='list_active_orders'))
    await callback_query.message.edit_text(
        f'{a.product.name} ({a.count}) | {a.status_text}\nОписание: {a.product.description}\nСтоимость: {a.product.price}\nСоздан: {a.created_at}\nСтатус обновлен {a.updated_at}',
        reply_markup=kb
    )