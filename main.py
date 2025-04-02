import asyncio
from aiogram.types import BotCommand, BotCommandScopeDefault
from bot import bot, dp, router, scheduler
from handlers.start import *
from handlers.notifications import *
from handlers.help import *
from handlers.dinner_time import *
from work_time.time_func import *

async def set_commands() -> None:
    commands = [
            BotCommand(command='start', description='Старт')
        ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

async def main():
    try:
        # scheduler.add_job(send_dinner_notification, 'cron', day_of_week='0-3', hour=17, args=(bot,))
        # scheduler.add_job(send_dinner_notification, 'cron', day_of_week='4', hour=16, args=(bot,))
        scheduler.start()
        dp.include_router(router)
        dp.startup.register(set_commands)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(e)

if __name__ == '__main__':  
    asyncio.run(main())