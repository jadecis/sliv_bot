from aiogram import Bot, Dispatcher, types
from config import bot_token, vk_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import logging
from src.database.db import Database
from loguru import logger
from vkbottle import API

bot = Bot(token=bot_token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
logger.disable("vkbottle")
db= Database("src/database/database.db")
api = API(token=vk_token)
html= types.ParseMode.HTML#<- &lt; >- &gt; &- &amp;

class Disc(StatesGroup):
    Q1= State()
    Q2= State()
    Q3= State()    