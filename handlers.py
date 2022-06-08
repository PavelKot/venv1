import  keybord as kb
import time
import requests
import win32timezone
import json
from main import bot,dp
import asyncio
from typing import Optional
from aiogram.types import Message
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
#from aiogram import State, StatesGroup
from config import  admin_id
from config import  API_link_streamko
from aiogram.types import  ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
#from aiogram.utils.callback_data import CallbackData
class Form(StatesGroup):
    peremennaya=State()
    peremennaya11=State()
asds1=0
z=111
argons='1233213'
argons1=''
DateData=[]
AOP=[]
DateDataForInform = ['Введите пожалуйста день от которого форм.статистику',
                     'Введите пожалуйста месяц до которого нужно форм.статистику',
                     'Введите пожалуйста день до которого нужно форм.статистику',' :)']
async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id[0],text="Bot starting")

@dp.message_handler(lambda message: message.text == '/help' or message.text == '/help@DIDInform_bot')
async  def echo(message:Message):
    z=0
    print(message.text)
    print(message.from_user.id)
    for i in admin_id:
        print(i)
        if message.from_user.id==i:
#    if message.text == '\help':
            text=f"/activate - if u use this command we should enter name of Company or User" \
                f'\n' "/start - This nothing do " \
                f'\n' "/new_client - This command proposise allowed work with this bot another people"
            await message.reply(text=text)
            z=1
    if z==0:
        await message.reply(text='I`m sorry but you can`t use this commands')
@dp.message_handler(lambda message: message.text == '/activate' or message.text == '/activate@DIDInform_bot' )
async def act(message:Message):
    z=0
    for i in admin_id:
        if i == message.from_user.id:
            await message.reply(text='User who need activations please enter +')
            z=1
    #Вписати запит на заповннення інформації
#     @dp.message_handler(content_types=["text"])
# async def do_something(message: Message):
#         argons=message.text
    if z == 0:
        await message.reply(text='I`m sorry but u don`t can activate this bot because you dont have privileges')
@dp.message_handler(lambda message: message.text == '+')
async def act(message:Message,z=z):
    print(z)
    z=0
    for i in admin_id:
        print('i'+str(i)+'messageFromUserID='+str(message.from_user.id))
        if i == message.from_user.id:
            await message.reply(text=f'Ammm {message.from_user.first_name} what you doing? Activating denied')
            z=1133
            return z
    if z==0:
        await message.reply(text=f'Hello {message.from_user.first_name} your ID {message.from_user.id} it`s added to my list')
        admin_id.append(message.from_user.id)
        print("AdminID ==>>>"+str(admin_id))
#@dp.message_handler(state=Add.test_state)
@dp.message_handler(lambda message: message.text == '/cdr' )
async def act(message:types.Message,state: FSMContext):
#    await message.reply(text='Please write data at ')
#    a = await message.answer(text='Please write data at ')
    z=11334
    for i in admin_id:
        if i==message.from_user.id:
            await message.answer(text='{i} Please write data at ')
            await Form.peremennaya.set()
            time.sleep(5)
            await message.answer(text='{i} Please write data to ')
            await Form.peremennaya11.set()
            time.sleep(5)
#            updates=requests.get(API_link_streamko+"/cdr/login?Tech_Pavel&password?oAm5i7Qa&with_unanswered=1&date_from=1539621667").json()
#    a=message.text

@dp.message_handler(lambda message: message.text == '/start' or message.text == '/start@DIDInform_bot')
async def start(message: types.Message):
    if message.from_user.id in admin_id:
        global asds1
        await bot.send_message(message.chat.id, 'Введите пожалуйста месяц от которого форм.статистику')
        await Form.peremennaya.set() # Устанавливаем состояние
        print(asds1)
    else:
        await bot.send_message(message.chat.id,'I`m sorry but u can`t use this command, please send request to @Pavel_PavelP he can add u to list')
@dp.message_handler(state=Form.peremennaya) # Принимаем состояние
async def cdr(message: types.Message, state: FSMContext, DateData=DateData,DataInform=DateDataForInform):
    async with state.proxy() as peremennaya1: # Устанавливаем состояние ожидания
        global asds1
        if asds1 == 3 :
            await message.reply(f" {DataInform[asds1]}")
            peremennaya1['peremennaya'] = message.text
            DateData.append(peremennaya1['peremennaya'])

            for i in DateData:
                print(i)
            await state.finish()
            operations(DateData)
            return
#            operations(DateData)
        await message.reply(f" {DataInform[asds1]}")
        print("ASDS1 =>",asds1)
        print(DataInform[asds1])
        peremennaya1['peremennaya'] = message.text
#        peremennaya1['peremennaya11'] = message.text
#        operations(peremennaya1)
#        print(peremennaya1['peremennaya'])
        print(peremennaya1['peremennaya'])
        print(int(peremennaya1['peremennaya']))
        DateData.append(peremennaya1['peremennaya'])
        for i in DateData:
            print("This is DateData ==>>>" + i)
#        print("enter dat =>")
        asds1 = asds1+1
#        operations(DateData)
        #    await state.finish() # Выключаем состояние
def operations(Appe=0):
    global asds1
    asds1=0
    print(int(time.time() - 2629743*5))
    a=int(Appe[0])*2592000 # month in sec
    b=int(Appe[1])*86400 # day in sec
    a1 = int(Appe[0])## month
    b1 = int(Appe[2])##month
    a2=int(Appe[1])##day
    b2=int(Appe[3])##day
    a1=int(a1*2629743) ##month in sec
    b1 = int(b1*2629743) ## month in sec
    a2 =  int(a2*86400) ##Day in sec
    b2 = int(b2*86400) ##Day in sec
    print("От количества секунд " )
    print(int(time.time() - (a1+a2)) )
    ARGUMs=(int(time.time() - (a1+a2)))
    print("До количества секунд ")
    print(int(time.time() - (b1+b2)))
    AGRUMs1=(int(time.time() - (b1+b2)))
    if (b1<a1):
        print("not correct")
    if (a1<b1):
        c=b1-a1
        c=c*30
        c=c+int(a2+b2)
        g=c*24
        sec=g*3600
        print("Summary in day ==>: "+str(c))
        print(f"Summary {c} days in Hours ==>"+str(g))
        print(f"Summary {g} hours in seconds ==>"+str(sec))
    print("a ==> Mont in sec : "+str(a))
    print(Appe[0] + '+' +  Appe[1])
    print(f"{Appe[0]} * 2592000")
    print(f"{Appe[1]} *86400")
#    print(a + ' + ' + b)
#    print(time.gmtime(c))
    print(str(ARGUMs) +' + ' + str(AGRUMs1))
    updates=requests.get(API_link_streamko+f"/cdr?_login=Tech_Pavel&_password=oAm5i7Qa&date_from={AGRUMs1}&date_to={ARGUMs}&with_unanswered=1").json()
    print(updates)
    global AOP
    AOP=updates
    orange(AGRUMs1,ARGUMs)
    #return  AGRUMs1, ARGUMs

#    send_to_admin()
#    obrobka_formatirovka()
def orange(a1a,b1b,tes=0) :
    @dp.message_handler(content_types=["text"])
    async def obrobka_formatirovka(message: types.Message):
#        await bot.send_message(message.chat.id,f'TES ==> {tes}')
        if(tes==1):
            await  bot.send_message(message.chat.id,'google.com')
            return 0
        global AOP
        #sdfasd=operations()
        #print(sdfasd)
        print("a1a===>"+str(a1a))
        print("b1b====>"+str(b1b))
        print(AOP['data'])
        example=AOP['data']
        count=0
        duration=0
        for i in example:
            print(i['calldate']+'\n'+i['dst']+'\n'+i['duration'])
            count+=1
            duration=duration + int(i['duration'])
       # rrr=time.gmtime(a1a)
       # rrr1=time.gmtime(b1b)

        print(f"Period at {time.gmtime(a1a).tm_mon}'month of year  {time.gmtime(a1a).tm_mday} day of month to {time.gmtime(b1b).tm_mon} month of year  {time.gmtime(b1b).tm_mday} day of month")

        await bot.send_message(chat_id=message.chat.id,text=f'all call in this period : {count} and all duration for this calls :'
                                               f' {duration}sec'
                                                f'\n'
                                                f'DURATION In minutes : {duration/60} ')
@dp.message_handler(commands=['inline'])
#async def handler(call: types.CallbackQuery, callback_data: dict, message: types.Message):
async def show_items(message: types.Message):
#    currency = call    back_data.get('currency')
#    print(currency)
#    keyboard1 = get_reply_markup(currency)
    await message.reply('It is buttons', reply_markup=kb.start_keyboard)
    kb.apelsin()



@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)
