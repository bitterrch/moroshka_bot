from aiogram import F
from aiogram.types import Message

from bot import router
from db.database_connect import Database
from keyboards.mainkeyboard import MainpageKeyboard

@router.message(F.text == MainpageKeyboard().buttons[4])
async def answer_yes_dinner(msg: Message) -> None:
    """This handler works when user taps 'Бегу в столовку'"""
    
    await Database().set_yes_dinner(msg.from_user.id)
    content = 'Ура! Морошка ждет тебя! Приятного аппетита :)'
    keyboard = await MainpageKeyboard().as_markup(msg.from_user.id)
    await msg.answer(content, reply_markup=keyboard)


@router.message(F.text == MainpageKeyboard().buttons[5])
async def answer_no_dinner(msg: Message) -> None:
    """This handler works when user taps 'Сегодня без столовки'"""

    await Database().set_yes_dinner(msg.from_user.id)
    content = 'Морошка тебя обязательно дождется...'
    keyboard = await MainpageKeyboard().as_markup(msg.from_user.id)
    await msg.answer(content, reply_markup=keyboard)