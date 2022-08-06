from imports import *

@dp.message_handler(commands=['order_select_shop'])
async def cmd_order_select_shop(msg: Message):
    await msg.answer('Выбери магазин')
