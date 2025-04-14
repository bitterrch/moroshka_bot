import datetime
import asyncio
from aiogram import Bot
from keyboards.mainkeyboard import MainpageKeyboard
from db.database_connect import Database

async def send_dinner_notification(bot: Bot) -> None:
    minutes = 60
    users = await Database().get_active_users()

    while minutes >= 0:
        for user in users:
            # проверка на случай если пользователь отказался от уведомлений во время работы джобы
            if await Database().user_is_active(user[0]) and await Database().is_get_notifications(user[0]):
                    
                # пользователь пропустил столовку
                if minutes == 0 and not await Database().is_yes_dinner(user[0]):
                    content = await Database().get_content(10060)
                    keyboard = await MainpageKeyboard().as_markup(user[0])

                # пользователь еще не отметил, идет он в столовку или нет
                elif not await Database().is_yes_dinner(user[0]):
                    content = await Database().get_content(10055)
                    keyboard = await MainpageKeyboard().dinner_time()
                    if minutes == 60:
                        content += '1 час!'
                    else:
                        content += f'{minutes} минут!'

                else:
                    continue

                await bot.send_message(user[0], content, reply_markup=keyboard)

        minutes -= 10
        await asyncio.sleep(600)

    for user in users:
        if await Database().is_yes_dinner(user[0]): await Database().set_no_dinner(user[0])
    