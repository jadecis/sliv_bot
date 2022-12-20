from loader import dp, bot, html, Disc, db
from aiogram.types import Message, CallbackQuery, MediaGroup
from aiogram.dispatcher import FSMContext
from src.keyboards.inline import accept_menu
from src.keyboards.reply import ras_menu
import asyncio
from aiogram.types import ReplyKeyboardRemove



    
@dp.message_handler(content_types='text', state=Disc.Q1)
async def get_text(msg: Message, state: FSMContext):
    await state.update_data(text=msg.text)
    await msg.answer("Отправь фото или видео\n\nПо окончанию нажми на кнопку «Закончить», если хочешь пропустить - нажми на кнопку «Пропустить»",
                     reply_markup=ras_menu)
    
    await Disc.Q2.set()

@dp.message_handler(content_types=['photo', 'video'], state=Disc.Q2)
async def application(msg: Message, state: FSMContext):
    data = await state.get_data()
    media_list= []
    if data.get('media') != None:
        for file_id in data.get('media'):
            media_list.append(file_id)
    if msg.content_type == 'photo':
        media= {
            'photo' : msg.photo[-1].file_id
        }
        media_list.append(media)
    if msg.content_type == 'video':
        media= {
            'video' : msg.video.file_id
        }
        media_list.append(media)   
    if msg.content_type == 'document':
        media= {
            'document' : msg.document.file_id
        }
        media_list.append(media) 
        
    await state.update_data(media= media_list)


@dp.message_handler(content_types='text', state=Disc.Q2)
async def q2_handler(msg: Message, state: FSMContext):
    if msg.text == 'Закончить':
        data = await state.get_data()
        media = MediaGroup()
        try:
            for file_id in data.get('media'):
                for k, v in file_id.items():
                    if k == 'photo':
                        media.attach_photo(v)
                    if k == 'video':
                        media.attach_video(v)
                    if k == 'document':
                        media.attach_document(v)
            await msg.answer_media_group(media=media)
            await msg.answer(text=data.get('text'),
                        reply_markup=accept_menu)
            await state.update_data(media= media)
            await Disc.Q3.set()
        except:
            await state.update_data(media=None)
            await msg.answer(text=f"Ошибка типа вложения. Пожалуйста, отправьте другой формат файла!")
            await Disc.Q2.set()
        

    if msg.text == 'Пропустить':
        data = await state.get_data()
        await msg.answer(text=data.get('text'),
                     reply_markup=accept_menu)
        await Disc.Q3.set()
    



@dp.callback_query_handler(text_contains= 'accept', state=Disc.Q3)
async def sabmit(call: CallbackQuery, state: FSMContext):
    if call.data.split('_')[1]== 'accept':
        await call.message.delete()
        msg_id=await call.message.answer(text='Рассылка началась', reply_markup=ReplyKeyboardRemove())
        data = await state.get_data('text')
        count_sender=0
        count_block=0
        for id in db.get_users_id():
            await asyncio.sleep(1)
            try:
                if data.get('media') != None:
                    await bot.send_media_group(chat_id=id[0], media=data.get('media'))
                    await asyncio.sleep(1)
                await bot.send_message(chat_id=id[0], text=data.get('text'))
                count_sender+=1
            except Exception as ex:
                count_block+=1
                continue
        await bot.delete_message(chat_id=call.message.chat.id, message_id=msg_id.message_id)
        await call.message.answer(text=f"Рассылка окончена.\n\nОтправленно: {count_sender} пользователям\nЗаблокировало: {count_block} пользователей")
        await state.finish()
    else:
        await state.finish()
        await call.message.answer(text=f"Введи текст для рассылки:\n\nЧтобы выйти нажми /start")
        await Disc.Q1.set()
    

     
    
    