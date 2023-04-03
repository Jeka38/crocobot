from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


words_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Посмотреть слово', callback_data='show_word')
            ],
            [
                InlineKeyboardButton(text='Изменить слово', callback_data='change_word')
            ]
        ]
)