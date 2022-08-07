import dotenv
dotenv.load_dotenv()

from aiohttp import web

import os
import orm
import aiogram
from aiogram.dispatcher.webhook import get_new_configured_app
import logging
# set logging format with module name
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = aiogram.Bot(token=os.environ.get('tg_token'))
dp = aiogram.Dispatcher(bot, storage=storage)
from commands import *

async def on_startup(app: web.Application):
    await dp.skip_updates()
    t = await bot.get_webhook_info()
    if t.url != os.environ.get('webhook_url'):
        await bot.delete_webhook()
        await bot.set_webhook(url=os.environ.get('webhook_url'))
async def on_shutdown(app: web.Application):
    await bot.delete_webhook()

async def http_handler(request: web.Request):
    try:
        mth = request.rel_url.query['method']
        order_id = request.rel_url.query.get('order_id', None)
        nst = int(request.rel_url.query.get('new_status', None))
        # print(mth, order_id, nst)
        if mth == 'update_status':
            order = api.order.get(order_id=order_id).response
            chat = order.client.chat_id
            from hashlib import md5
            # print(chat, order)
            code = md5(str('Coffee:' + str(order.id)).encode()).hexdigest()[:4]
            # print(order.statuses[nst])
            text = f'Заказ {order.id} был обновлен\n{order.product.name} ({order.count})\nНовый статус: {order.statuses[nst]}'
            if nst == 3:
                text += f'\nДля получения используйте QR или код: {code}'
            await bot.send_message(
                chat,
                text=text
            )
            if nst == 3:
                import qrcode
                from io import BytesIO
                buffered = BytesIO()
                qrcode.make(code).save(buffered, format="JPEG")
                await bot.send_photo(chat_id=chat, photo=buffered.getvalue())
    except Exception as e:
        print('exc', e)

    return web.Response(text='OK')

if __name__ == '__main__':
    import imports
    logging.info(str(dp.message_handlers.handlers))
    application = get_new_configured_app(dispatcher=dp, path='/webhook')
    application.on_startup.append(on_startup)
    application.on_shutdown.append(on_shutdown)
    application.router.add_route('GET', '/api', http_handler)
    # application.router.add_route()
    web.run_app(application, host='0.0.0.0', port=os.environ.get('port'))
