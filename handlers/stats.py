from aiogram.types import Message
from create_bot import dp, datebase


@dp.message_handler(commands=['score'])
async def get_score(message: Message):
    player_id = message.from_user.id
    score = datebase.get_score(chat_id=message.chat.id, player_id=player_id)
    await message.answer(
        text=f'{datebase.get_player_name(player_id)}'
             f'\nОчков в этом чате: {score}'
    )


@dp.message_handler(commands=['scoretable'])
async def get_score_table(message: Message):
    table = datebase.get_score_table(chat_id=message.chat.id)
    text = 'Таблица топ10 игроков этого чата:'
    for score in table:
        text += f'\n{score[0]} - {score[1]}'
    await message.answer(text)
