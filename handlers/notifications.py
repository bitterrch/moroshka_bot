from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot import router
from db.database_connect import Database
from keyboards.mainkeyboard import MainpageKeyboard

@router.message(F.text == MainpageKeyboard().buttons[1])
async def start_get_notifications(msg: Message, state:FSMContext) -> None:
    """This handler works when user taps 'Хочу получать уведомления'"""
    data = await state.get_data()
    # пользователь уже получает уведомления
    if await Database().is_get_notifications(msg.from_user.id):
        content_id = 10015
    # пользователь еще не получает уведомления
    else:
        await Database().start_get_notifications(msg.from_user.id)
        if not await Database().user_is_active(msg.from_user.id):
            if data and data['old'] == True:
                content_id = 10020
            else:
                content_id = 10050
        else:
            content_id = 10020

        await Database().make_user_active(msg.from_user.id)
        await state.update_data(old = False)

    keyboard = await MainpageKeyboard().as_markup(msg.from_user.id)
    content = await Database().get_content(content_id)
    await msg.answer(content, reply_markup=keyboard)

@router.message(F.text == MainpageKeyboard().buttons[2])
async def stop_get_notifications(msg: Message) -> None:
    """This handler works when user taps 'Не хочу получать уведомления'"""

    # пользователь не получает уведомления
    if not await Database().is_get_notifications(msg.from_user.id):
        content_id = 10025
    # пользователь получает уведомления
    else:
        await Database().stop_get_notifications(msg.from_user.id)
        await Database().make_user_inactive(msg.from_user.id)
        content_id = 10030

    keyboard = await MainpageKeyboard().as_markup(msg.from_user.id)
    content = await Database().get_content(content_id)
    await msg.answer(content, reply_markup=keyboard)