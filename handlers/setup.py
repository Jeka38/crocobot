import logging
from aiogram.types import Message
from keyboards.inline.game import words_keyboard
from create_bot import dp, datebase


async def setup_game(message: Message):
    chat_id = message.chat.id
    if not datebase.chat_exists(chat_id):
        datebase.add_chat(chat_id, chat_name=message.chat.full_name)
        logging.info(f'Chat with id = {chat_id} added to database')
    if datebase.in_play(chat_id=chat_id):
        await message.answer(
            text=f'Игра уже в процессе!\n{datebase.get_speaker_name(chat_id)} - объясняющий',
            reply_markup=words_keyboard,
            disable_notification=True
        )
        return
    await set_categories(message=message)


#
@dp.message_handler(commands=['categories'])
async def set_categories(message: Message):
    await message.answer(
        text='Используйте /play чтобы запустить игру.',
        disable_notification=True
    )
