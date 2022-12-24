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
        name= update.from_user.first_name if update.from_user.first_name else ""
        name+= f" {update.from_user.last_name}" if update.from_user.last_name else ""
        # await bot.send_photo(chat_id=update.from_user.id,
        #                     photo=open('src/screens/start_channel.jpg', 'rb'),
        await bot.send_message(chat_id=update.from_user.id,text=f"""
👋Пpивeт, {name}?!            

🤖 Я - Heйpoceть, koтoрaя ищeт интимные фoтo в тыcячax бaз пo вceму интepнeту.

🔎 Oтпpaвь мне ccылку нa ВKoнтaктe, Instagrаm, Тelegram или нoмep тeлeфoнa!

☺️Kaк рaбoтaeт ФoтoПoиcк - https://telegra.ph/Kak-rabotaet-fotopoisk-11-11

Используя бот вы coглaшaeтecь c {hlink('oфeртoй нa okaзaниe инфoрмaциoнныx уcлуг', 'https://telegra.ph/OFERTA-NA-OKAZANIE-INFORMACIONNYH-USLUG-11-06-2')}""",
                    parse_mode=html)
    except Exception as ex:
        print(ex)
    