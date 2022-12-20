from loader import dp, db, bot,html 
from aiogram import executor
from src.parse.scrapp import get_inf_inst, get_inf_tg, get_inf_vk
from aiogram.types import BotCommand 
import random
import asyncio
from aiogram.utils.markdown import hlink
from src.handlers import main
from src.handlers import rassilka
# from src.handlers import payment 
from src.handlers import chanel

import aioschedule
    

async def sliv_ras():
    result= db.select_sliv(status="not payment")
    for sliv in result:
        if sliv[1].__contains__('vk.com'):
            result= await get_inf_vk(sliv[1])
            print(result)
            res= result[0]
        if sliv[1].__contains__('instagram'):
            link_parse= sliv[1].split('/')[-1]
            res= await get_inf_inst(link_parse)
        if sliv[1].__contains__('t.me'):
            res= get_inf_tg(sliv[1])
        print(res)
        try:
            await bot.send_photo(chat_id=sliv[0] , photo=open(f"src/screens/screen_ras/{random.randint(1,5)}.jpg", "rb"),
    caption=f"""
❗️СРОЧНО❗️

✅Только что с аккаунта {hlink(res, sliv[1])}, было отправлено исчезающее фото!
Диалог сохранить не удалось, но фоточки остались😱

<code>🔥Чтобы проверить, жми</code> /start""",
parse_mode= html)
        except Exception as ex:
            print(ex)
            continue

async def scheduler():
    aioschedule.every(2).hours.do(sliv_ras)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)



async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand("start", "restart bot")
    ])
    asyncio.create_task(scheduler())
    

#запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=set_default_commands)