from aiogram.dispatcher.filters.builtin import AdminFilter
from aiogram.types import Message
from create_bot import dp, g


@dp.message_handler(AdminFilter(), commands=['categories'])
async def set_categories(message: Message):
    await message.answer(
        text='Используйте /play для запуска игры',
        disable_notification=True
    )


@dp.message_handler(
    lambda message: g.in_play(chat_id=message.chat.id),
    commands=['stop']
)
async def stop_game(message: Message):
    g.change_state(chat_id=message.chat.id, state=0)
    await message.answer(
        text='Игра остановлена',
        disable_notification=True
    )
