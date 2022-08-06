from imports import *

@dp.message_handler(commands=['/profile'])
async def cmd_profile(msg: Message):
    await msg.answer('Профиль')
