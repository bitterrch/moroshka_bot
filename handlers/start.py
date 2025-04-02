from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot import router
from db.database_connect import Database
from keyboards.mainkeyboard import MainpageKeyboard

import datetime
 
@router.message(CommandStart())
async def start(msg: Message, state: FSMContext):
    await state.update_data(old = False)

    # пользователь есть в БД
    if await Database().user_exists(msg.from_user.id):
        # пользователь либо пользуется ботом, либо еще не выбрал, хочет ли уведы получать
        if await Database().user_is_active(msg.from_user.id):
            # пользуется
            if await Database().is_get_notifications(msg.from_user.id):
                content_id = 10005
            # еще не выбрал
            else:
                content_id = 10000
        # зашел после того, как перестал пользоваться
        else:
            content_id = 10010
            await state.update_data(old = True)

    # пользователя нет в БД
    else:
        content_id = 10000
        await Database().add_user(msg)


    keyboard = await MainpageKeyboard().as_markup(msg.from_user.id)

    content = await Database().get_content(content_id)
    await msg.answer(content, reply_markup=keyboard)
    