from auth import TG_KEY, WEA_KEY
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from weather import get_weather
from course import get_cours

bot = Bot(token=TG_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands=["help"])
async def start_command(message: types.Message):
    print(message)
    print(message.content_type)
    print(message.text)        
    await message.reply("/p    /c")


@dp.message_handler(commands=["p"])
async def start_command(message: types.Message):
    mes = message.text.split()
    #mes = message.text
    print(mes)
    if len(mes) == 1:
        button_get_geo = KeyboardButton('Отправить свою локацию 🗺️', request_location=True) 
        greet_geo = ReplyKeyboardMarkup( resize_keyboard=True, one_time_keyboard=True)
        greet_geo.add(button_get_geo)        
        await message.reply("введите город в формате /p город",reply_markup=greet_geo)     
    else:
        r = get_weather(mes[1],WEA_KEY) 
        await message.reply(r, parse_mode=types.ParseMode.HTML)
        
@dp.message_handler(content_types=['location'])
async def handle_loc(message):
    print(message.location)
    await message.reply("OK", parse_mode=types.ParseMode.HTML)
'''прилетело то что надо:
{'longitude': xx.xxxxxx, 'latitude': yy.yyyyyy}
'''
@dp.message_handler(commands=["c"])
async def start_command(message: types.Message):
    mes = message.text.split()     
    if len(mes) == 1:
        button_dol = KeyboardButton('/c DOLLAR')
        button_eu = KeyboardButton('/c EURO') 
        greet_kb = ReplyKeyboardMarkup( resize_keyboard=True, one_time_keyboard=True)
        greet_kb.add(button_dol)
        greet_kb.add(button_eu)
        await message.reply("введите команду  /c валюта", reply_markup=greet_kb) 
    else:
        await message.reply(get_cours(mes[1]))     
   


            
@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def process_photo_command(message: types.Message):
    '''print("photo")
    print(message)
    print(message.content_type)
    print(message.text)        
    await message.reply("Media") 
    # Убедитесь, что каталог /tmp/somedir существует!
    await message.photo[-1].download(destination="/tmp/somedir/")'''
    await message.photo[-1].download('test.jpg')

@dp.message_handler()    
async def echo_message(message: types.Message):       
    print("ALL")   
    await message.reply("All") 


if __name__ == "__main__":
    print("start")
    executor.start_polling(dp)
    #get_cours()
    #get_weather("Барнаул",WEA_KEY)