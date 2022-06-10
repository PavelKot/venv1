from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram import bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import  handlers as han
import ExampleAPIstreamco
from main import bot,dp
from aiogram.types import  ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
#some code



inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Вторая кнопка', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
@dp.callback_query_handler(lambda callback_query: True)
async def process_callback_button11(callback_query: types.CallbackQuery):
#    print(callback_query.data)
#    for i in callback_query:
#        print(i)
    await bot.answer_callback_query(callback_query.id,"Hello")
    print(callback_query.data)
    if callback_query.data == 'button1':
        print('ass')
        await  bot.send_message(callback_query.message.chat.id, text='You best!')
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
#    await bot.send_message(callback_query.message.chat.id,'Hello my friend')

studyboi = InlineKeyboardButton('CDR statistics',callback_data='button1')
studyboi1 = KeyboardButton(f'Hello ')
#InlineKeyboardButton('text1', url='google.com')
asdas=InlineKeyboardMarkup().add(studyboi)
arr = ['CDR statistics','Billing','Answer Calls']
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(studyboi1)
#asrr=rReplyKeyboardMarkup(resize_keyboard=True)
#for i in arr:
#    asrrr = InlineKeyboardButton(i)
#    start_keyboard.add(asrrr)
#studyboi2 = ReplyKeyboardMarkup('text2',one_time_keyboard=True)

#Button(Const("Useles Button"),id="nothing")
#@dp.message_handler(commands=['1'])
#async def process_callback_button1(message: types.Message,callback_query: types.CallbackQuery):
#    await message.reply("Первая инлайн кнопка !",reply_markup=studyboi)
#    await bot.answer_callback_query(callback_query.id,message='ass')
#    await bot.answer_callback_query(call.id)
#    await bot.send_message(call.from_user.id, 'Нажата первая кнопка!')
def apelsin():
#    mesage : types.Message
    @dp.message_handler(lambda message: message.text == 'CDR statistics')
    async def anal(mesage : types.Message):
#    bot.send_message(mesage.chat.id,'google.com',reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(mesage.chat.id, 'This is function on keybord.py',reply_markup=types.ReplyKeyboardRemove())

    @dp.message_handler(lambda message: message.text == 'text1')
    async def anal1(mesage : types.Message):
        await bot.send_message(mesage.chat.id, 'This is another function ',reply_markup=types.ReplyKeyboardRemove())
