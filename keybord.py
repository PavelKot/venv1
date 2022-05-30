from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram import bot,Dispatcher,executor,types
from aiogram.types import  ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format
import  handlers as han
from main import bot,dp
#some code

studyboi = InlineKeyboardButton('text', url='google.com')
studyboi1 = InlineKeyboardButton('text1', url='google.com')
#studyboi2 = ReplyKeyboardMarkup('text2',one_time_keyboard=True)
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(studyboi).add(studyboi1)
#Button(Const("Useles Button"),id="nothing")
#def apelsin():
#    mesage : types.Message
#    @dp.message_handler(content_types=["text"])
#    async def anal(mesage : types.Message):
#    bot.send_message(mesage.chat.id,'google.com',reply_markup=types.ReplyKeyboardRemove())
#        await bot.send_message(mesage.chat.id, 'This is function on keybord.py')
