from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards import Keyboard
from db.database_connect import Database
class MainpageKeyboard(Keyboard):
    """Main page keyboard"""

    def __init__(self) -> None:
        self.buttons = {
            1: "Хочу получать уведомления",
            2: "Не хочу получать уведомления",
            
            4: "Бегу в столовую!",
            5: "Сегодня без столовки",

            3: "Помощь",

            6: "Когда там ужин?",
            7: "Когда приходят уведомления?",
            8: "Назад"
        }


    async def as_markup(self, user_id: int) -> ReplyKeyboardMarkup:
        kb_list = []

        if not await Database().is_get_notifications(user_id):
            kb_list.append([KeyboardButton(text=self.buttons[1])])
        else:
            kb_list.append([KeyboardButton(text=self.buttons[2])])

        kb_list.append([KeyboardButton(text=self.buttons[3])])
        
        keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

        return keyboard
    
    async def dinner_time(self) -> ReplyKeyboardMarkup:
        kb_list = [
            [KeyboardButton(text=self.buttons[4])],
            [KeyboardButton(text=self.buttons[5])],
            [KeyboardButton(text=self.buttons[2])]
        ]

        keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

        return keyboard
    
    async def for_help(self) -> ReplyKeyboardMarkup:
        kb_list = [
            [KeyboardButton(text=self.buttons[6])],
            [KeyboardButton(text=self.buttons[7])],
            [KeyboardButton(text=self.buttons[8])]
        ]

        keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

        return keyboard
    