import json

from imports import *
from api import api

from aiogram.dispatcher.filters.state import State, StatesGroup


class FormOrder(StatesGroup):
    shop_id = State()
    product_id = State()
    count = State()

@dp.message_handler(commands=['order_select_shop'])
async def cmd_order(msg: Message):
    a = api.shop.get_all()
    await FormOrder.shop_id.set()
    keyboard = InlineKeyboardMarkup(row_width=1)
    for i in a.response:
        i = i[0]
        keyboard.add(InlineKeyboardButton(
            text=i.name,
            callback_data=f'shop_id_{i.id}'
        ))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='cancel'))
    await msg.answer('Выберите магазин', reply_markup=keyboard)


@dp.callback_query_handler(text_startswith=['shop_id_', 'cancel'], state=FormOrder.shop_id)
async def callback_order_select_shop(
        callback_query: CallbackQuery,
        state: FSMContext):
    if callback_query.data == 'cancel':
        await state.finish()
        await callback_query.answer('Отменено')
        from commands import cmd_menu
        await cmd_menu(callback_query.message)
        return
    shop_id = int(callback_query.data.split('_')[-1])
    async with state.proxy() as p:
        p['shop_id'] = shop_id
    a = api.shop.get_products(shop_id=shop_id)
    keyboard = InlineKeyboardMarkup(row_width=1)
    for i in a.response:
        i = i[0]
        keyboard.add(InlineKeyboardButton(
            text=i.name,
            callback_data=f'product_id_{i.id}'
        ))
    await FormOrder.product_id.set()
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='cancel'))
    await callback_query.message.edit_text(
        'Выберите продукт',
        reply_markup=keyboard
    )

@dp.callback_query_handler(text_startswith=['product_id_', 'cancel'], state=FormOrder.product_id)
async def callback_order_select_product(
        callback_query: CallbackQuery,
        state: FSMContext):
    if callback_query.data == 'cancel':
        await state.finish()
        await callback_query.answer('Отменено')
        from commands import cmd_menu
        await cmd_menu(callback_query.message)
        return
    product_id = int(callback_query.data.split('_')[-1])
    async with state.proxy() as p:
        p['product_id'] = product_id
    await FormOrder.count.set()
    keyboard = InlineKeyboardMarkup(row_width=5)
    s = []
    for i in range(1, 6):
        s.append(InlineKeyboardButton(
            text=str(i),
            callback_data=f'count_{i}'
        ))
    keyboard.add(*s)
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='cancel'))
    await callback_query.message.edit_text(
        'Выберите количество', reply_markup=keyboard
    )

@dp.callback_query_handler(text_startswith=['cancel'])
async def cancel(callback_query: CallbackQuery,
        state: FSMContext):
    from commands import cmd_menu
    await cmd_menu(callback_query.message)

@dp.callback_query_handler(text_startswith=['count_', 'cancel'], state=FormOrder.count)
async def callback_order_select_count(
        callback_query: CallbackQuery,
        state: FSMContext):
    if callback_query.data == 'cancel':
        await state.finish()
        await callback_query.answer('Отменено')
        from commands import cmd_menu
        await cmd_menu(callback_query.message)
        return
    count = int(callback_query.data.split('_')[-1])
    async with state.proxy() as p:
        shop_id = p['shop_id']
        product_id = p['product_id']
    await state.finish()
    # from keyboards import keyboard_menu

    api.order.add(
        client_id=api.client.get(chat_id=callback_query.message.chat.id).response.id,
        shop_id=shop_id,
        product_id=product_id,
        count=count
    )
    await callback_query.message.edit_text(
        'Заказ оформлен',
        reply_markup=InlineKeyboardMarkup()
    )
    from commands import cmd_menu
    await cmd_menu(callback_query.message)


