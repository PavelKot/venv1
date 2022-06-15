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


fck =[]
inline_btn_1 = InlineKeyboardButton('Указать период', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Вторая кнопка', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Январь', callback_data='button3')
inline_btn_4 = InlineKeyboardButton('Февраль', callback_data='button4')
inline_btn_5 = InlineKeyboardButton('Март', callback_data='button5')
inline_btn_6 = InlineKeyboardButton('Апрель', callback_data='button6')
inline_btn_7 = InlineKeyboardButton('Май', callback_data='button7')
inline_btn_8 = InlineKeyboardButton('Июнь', callback_data='button8')
inline_kb1 = InlineKeyboardMarkup().insert(inline_btn_1).insert(inline_btn_2)
inline_kb2 = InlineKeyboardMarkup()
inline_kb3 = InlineKeyboardMarkup()
inline_kb4 = InlineKeyboardMarkup()
inline_kb2.add(inline_btn_3,inline_btn_4,inline_btn_5,inline_btn_6,inline_btn_7,inline_btn_8)
Tom1=0
Tod1=0
buttton=0
Atm=0
Atd=0
Atd1=0
start=0
maximus=0

@dp.callback_query_handler(lambda callback_query: True)
async def process_callback_button11(callback_query: types.CallbackQuery):
#    global Tom1,Tod1,Atm,Atd
    if callback_query.data=='button8' :
        print('WoW')
    global start,buttton,Atd1,Atd,Atm,Tom1,Tod1,maximus
    await bot.answer_callback_query(callback_query.id,' ')
    print("LION")
    print(callback_query.data)
    Atd1 = callback_query.data
    print(Atd1)
    print('Atm ==>'+str(Atm))
    print('Tom1 ==>>'+str(Tom1))
    if buttton==1:
        Atd=callback_query.data
        callback_query.data='button1'
        buttton=0
    elif buttton==2:
        Tod1=callback_query.data
        start=1
    if callback_query.data == 'button1':
        await  bot.send_message(callback_query.message.chat.id, text='You best!')
#        await bot.answer_callback_query(callback_query.id,text='Button3')
        await  bot.send_message(callback_query.message.chat.id, text='Месяц',reply_markup=inline_kb2)
    if callback_query.data == 'button3':
        if Atm != 0:
            Tom1=1
        if Atm == 0:
            Atm = 1
        maximus=31
    elif callback_query.data == 'button4': #02 month
            if Atm != 0:
                Tom1=2
            if Atm == 0:
                Atm = 2
            maximus=28
            print('b')
    elif callback_query.data == 'button5': #03 month
            if Atm != 0:
                Tom1=3
            if Atm == 0:
                Atm = 3
            maximus=31
            print('c')
    elif callback_query.data == 'button6': #04 month
            if Atm != 0:
                Tom1=4
            if Atm == 0:
                Atm = 4
            maximus=30
            print('t')
    elif callback_query.data == 'button7': #05 month
        if Atm != 0:
            Tom1=5
        if Atm == 0:
            Atm = 5
        maximus=31
        print('b')
    elif callback_query.data == 'button8': #06 month
        print('In elif callback_query.data == button8')
        if Atm != 0:
            Tom1=6
        elif Atm == 0:
            Atm = 6

        print('Atm',Atm)
        print('Tom1', Tom1)
        maximus=30
        print('h')
        print(callback_query.data)
        callback_query.data='button8'
    if Atm > 0 and Tom1==0 and start == 0 and Atd==0:
        i=1
        while i <= maximus:
            if i<10:
                inline_kb3.insert(InlineKeyboardButton(f'{i}',callback_data=f'{i}'))
                i+=1
                continue
            inline_kb3.insert(InlineKeyboardButton(f'{i}',callback_data=f'{i}'))
            i+=1
        await bot.send_message(callback_query.message.chat.id,'День',reply_markup=inline_kb3)
        print(callback_query.data)
        buttton=1
#    elif callback_query.data!='button1':
    if Atm>0 and Tom1>0 and start == 0:
            i=1
            while i <= maximus:
                if i<10:
                    inline_kb4.insert(InlineKeyboardButton(f'{i}',callback_data=f'{i}'))
                    i+=1
                    continue
                inline_kb4.insert(InlineKeyboardButton(f'{i}',callback_data=f'{i}'))
                i+=1
            await bot.send_message(callback_query.message.chat.id,'День',reply_markup=inline_kb4)
            print(callback_query.data)
            buttton=2
    if start==1:
        print('start')
        print(Atm,Atd,Tom1,Tod1)
        Atm=int(Atm)
        Atd=int(Atd)
        Tom1=int(Tom1)
        Tod1=int(Tod1)
        print(Atm,Atd,Tom1,Tod1)
        await bot.send_message(callback_query.message.chat.id,'Please waite up to 20 sec: ')
        #agrus=(ExampleAPIstreamco.anolus(Atm,Atd,Tom1,Tod1))
        agrus1=(ExampleAPIstreamco.anolus1(Atm,Atd,Tom1,Tod1))
        print(agrus1)
        for i in agrus1:
            print(i)
        await bot.send_message(callback_query.message.chat.id,'CDR  statistic: ')
        await bot.send_message(callback_query.message.chat.id,f'Answer call:{agrus1[0]} | No Answer call : {agrus1[1]}  |'
                                                              f'Count Duration in sec all Answer : {agrus1[2]} sec | Count all calls: TLC_group2_head2 : {agrus1[3]} ')
        #for i in agrus1:
            #print(i)
            #print(i['calldate'], i['dst'] , i['duration'])
            #shit=i['calldate']
            #shit1 = i['dst']
            #shit2=i['duration']
            #shit3=i['billsec']
            #await bot.send_message(callback_query.message.chat.id,f'calldate: {shit} dst: {shit1} duration: {shit2} billsec: {shit3}')
        Atm=0
        Atd=0
        Tod1=0
        Tom1=0
        start=0
        buttton=0
        print('finish')

    else:
        pass
