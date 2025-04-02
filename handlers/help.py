from aiogram import F
from aiogram.types import Message

from bot import router
from db.database_connect import Database
from keyboards.mainkeyboard import MainpageKeyboard

@router.message(F.text == MainpageKeyboard().buttons[3])
async def start_get_notifications(msg: Message) -> None:
    """This handler works when user taps 'Помощь'"""

    keyboard = await MainpageKeyboard().for_help()
    content = await Database().get_content(10035)
    await msg.answer(content, reply_markup=keyboard)


@router.message(F.text == MainpageKeyboard().buttons[6])
async def when_dinner(msg: Message) -> None:
    """This handler works when user taps 'Когда там ужин?'"""

    keyboard = await MainpageKeyboard().for_help()
    content = 'Здесь будет выводиться, сколько времени осталось до ужина))'
    await msg.answer(content, reply_markup=keyboard)


@router.message(F.text == MainpageKeyboard().buttons[7])
async def when_dinner(msg: Message) -> None:
    """This handler works when user taps 'Когда приходят уведомления?'"""

    keyboard = await MainpageKeyboard().for_help()
    content = await Database().get_content(10040)
    await msg.answer(content, reply_markup=keyboard)


@router.message(F.text == MainpageKeyboard().buttons[8])
async def when_dinner(msg: Message) -> None:
    """This handler works when user taps 'Назад'"""

    keyboard = await MainpageKeyboard().as_markup(msg.from_user.id)
    content = await Database().get_content(10045)
    await msg.answer(content, reply_markup=keyboard)