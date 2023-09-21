from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import asyncio 
from config import TOKEN
from handlers import router


async def on_startup(bot: Bot):
    print('Бот был успешно запущен!')
    await bot.delete_webhook(drop_pending_updates=True)


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')