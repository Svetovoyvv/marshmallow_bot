from imports import *

@dp.message_handler(commands=['active_orders'])
async def cmd_active_orders(msg: Message):
    await msg.answer('Активные заказы')
