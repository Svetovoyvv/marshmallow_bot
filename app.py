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



bot = aiogram.Bot(token=os.environ.get('tg_token'))
dp = aiogram.Dispatcher(bot)
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
    print(await request.json())
    return web.Response(text='OK')

if __name__ == '__main__':

    logging.info(str(dp.message_handlers.handlers))
    application = get_new_configured_app(dispatcher=dp, path='/webhook')
    application.on_startup.append(on_startup)
    application.on_shutdown.append(on_shutdown)
    application.router.add_route('GET', '/api', http_handler)
    # application.router.add_route()
    web.run_app(application, host='0.0.0.0', port=os.environ.get('port'))
