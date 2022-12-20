from aiogram.types import ChatJoinRequest
from loader import dp, bot, html, db
from aiogram.utils.markdown import hlink
from src.keyboards.inline import search_inline, start_menu
from src.keyboards.reply import search_reply



@dp.chat_join_request_handler()
async def start1(update: ChatJoinRequest):
    if not(db.user_exist(update.from_user.id, 'users')):
        db.add_user(update.from_user.id, update.from_user.username)
    try:
        await update.approve()
        # await bot.send_photo(chat_id=update.from_user.id,
        #                     photo=open('src/screens/start_channel.jpg', 'rb'),
        await bot.send_message(chat_id=update.from_user.id,
                            text=f"""
<b>Привет, я бот, который найдёт фото любой девушки, которая хоть раз скидывала кому-то интим фото в ВК, Телеграм или Instagram🔥</b>

👇🏻Проверь свою подругу 💋

/start /start /start /start""",
                    parse_mode=html)
    except Exception as ex:
        print(ex)
    