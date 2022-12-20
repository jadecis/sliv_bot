from loader import db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def select_payment(price, step):
    payments= InlineKeyboardMarkup(row_width=1)
    
    payments.add(
        InlineKeyboardButton('Оплата с карты 💳', callback_data=f'select_{step}_card_{price}'),
        InlineKeyboardButton('Оплата с QIWI 🥝', callback_data=f'select_{step}_qiwi_{price}'),
        InlineKeyboardButton('Оплата с ЮMoney ✡️', callback_data=f'select_{step}_ymoney_{price}'),
        InlineKeyboardButton('Отзывы 💋', url='https://t.me/bugph')
    )
        
    return payments
    

def payment(price, step, bill_id, url):
    pay_button= InlineKeyboardMarkup(row_width=2)

    pay_button.insert(
        InlineKeyboardButton(f'💳 ОПЛАТИТЬ {price}₽', url=url)    
    )
    pay_button.add(
        InlineKeyboardButton('✅ Проверить платеж', callback_data=f'check_bill{str(bill_id)}_{step}')
    )
    pay_button.add(
        InlineKeyboardButton('⬅️ Другой способ оплаты', callback_data=f'back_{price}_{step}'),
        InlineKeyboardButton('Отзывы 💋', url='https://t.me/bugph')
        
    )
    return pay_button

first_step= InlineKeyboardMarkup(row_width=1)

# first_step.add(
#     InlineKeyboardButton('Приобрести 💸 | 199₽', callback_data='tariff_199'),
#     InlineKeyboardButton('Удалить из базы 🗑 | 199₽', callback_data='tariff_199'),
#     InlineKeyboardButton('Подписка 3 часа 🔒 | 249₽', callback_data='tariff_249'),
#     InlineKeyboardButton('Навсегда 💸 | 449₽', callback_data='tariff_449')
# )
first_step.add(
    InlineKeyboardButton('Приобрести 💸 | 199₽', url=f"{db.get_link()}"),
    InlineKeyboardButton('Удалить из базы 🗑 | 199₽', url=f"{db.get_link()}"),
    InlineKeyboardButton('Подписка 3 часа 🔒 | 249₽', url=f"{db.get_link()}"),
    InlineKeyboardButton('Навсегда 💸 | 449₽', url=f"{db.get_link()}"),
    InlineKeyboardButton('Отзывы 💋', url='https://t.me/bugph')
)

start_menu= InlineKeyboardMarkup(row_width=1)

start_menu.add(
    InlineKeyboardButton('Начать поиск 🔎', callback_data= 'search'),
    InlineKeyboardButton('Инструкция 📄', url='https://telegra.ph/Kak-rabotaet-fotopoisk-11-11'),
    InlineKeyboardButton('Отзывы 💋', url='https://t.me/bugph')
    
)

accept_menu= InlineKeyboardMarkup(row_width=2)
accept_menu.add(
    InlineKeyboardButton('✅ Подтвердить', callback_data='accept_accept'),
    InlineKeyboardButton('✏️ Изменить', callback_data='accept_cancel')
)