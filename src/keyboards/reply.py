from aiogram.types import ReplyKeyboardMarkup

search_reply= ReplyKeyboardMarkup(resize_keyboard=True)
search_reply.add('🔎 Поиск')

ras_menu= ReplyKeyboardMarkup(resize_keyboard=True)

ras_menu.add('Пропустить', 'Закончить')