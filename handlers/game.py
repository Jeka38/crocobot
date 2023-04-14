from aiogram.types import CallbackQuery, Message
from keyboards.inline.game import words_keyboard
from create_bot import dp, datebase, logging


async def init_game(message: Message):
    chat_id = message.chat.id
    player_id = message.from_user.id
    if not datebase.player_exists(player_id):
        datebase.add_player(player_id=player_id, player_name=message.from_user.mention)
        logging.info(f'User with id = {player_id} added to database')
    datebase.set_correct_word(chat_id)
    datebase.set_speaker(chat_id=chat_id, speaker_id=message.from_user.id)
    await message.answer(
        text=f'{datebase.get_speaker_name(chat_id)} - объясняющий',
        reply_markup=words_keyboard,
        disable_notification=True
    )


@dp.message_handler(commands=['play'])
async def start_game(message: Message):
    chat_id = message.chat.id
    if datebase.in_play(chat_id=chat_id):
        await message.answer(
            text=f'Игра уже в процессе!\n{datebase.get_speaker_name(chat_id)} - объясняющий',
            reply_markup=words_keyboard,
            disable_notification=True
        )
        return
    await init_game(message=message)
    datebase.change_state(chat_id=chat_id, state=1)


@dp.callback_query_handler(text='show_word')
async def show_word(call: CallbackQuery):
    chat_id = call.message.chat.id
    if call.from_user.id != datebase.get_speaker_id(chat_id=chat_id):
        await call.answer(text='Вы не ведущий и не можете смотреть слово', show_alert=True)
        return
    text = datebase.get_correct_word(chat_id=chat_id)
    await call.answer(text=text, show_alert=True)


@dp.callback_query_handler(text='change_word')
async def change_word(call: CallbackQuery):
    chat_id = call.message.chat.id
    if call.from_user.id != datebase.get_speaker_id(chat_id=chat_id):
        await call.answer(text='Вы не ведущий и не можете изменять слово', show_alert=True)
        return
    datebase.set_correct_word(chat_id=chat_id)
    await show_word(call=call)


@dp.message_handler(
    lambda message:
    datebase.chat_exists(chat_id=message.chat.id) and
    datebase.in_play(chat_id=message.chat.id) and
    datebase.get_correct_word(message.chat.id).lower() in message.text.lower() and
    message.from_user.id != datebase.get_speaker_id(chat_id=message.chat.id)
)
async def correct_word(message: Message):
    chat_id = message.chat.id
    player_id = message.from_user.id
    await message.reply(text='Ответ верный!', disable_notification=True)
    await init_game(message)
    if not datebase.score_exists(chat_id=chat_id, player_id=player_id):
        datebase.add_score(chat_id=chat_id, player_id=player_id)
        logging.info(
            f'Score of player with {player_id} id in {chat_id} chat added to database'
        )
    datebase.increase_score(chat_id=chat_id, player_id=player_id)
