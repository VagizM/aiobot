from auth import TG_KEY, WEA_KEY
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from weather import get_weather, get_weather_coord
from course import get_cours
import datetime
import os

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
    print(message.location["latitude"])
    print(message.location["longitude"])    
    r = get_weather_coord(lat=message.location["latitude"], lon=message.location["longitude"]) 
    await message.reply(r, parse_mode=types.ParseMode.HTML)
'''прилетело то что надо:
{"latitude": 66.396693, "longitude": 77.16208}
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
    if message["caption"] == None: 
        s=""
    else:      
        
        s = "".join(filter(str.isalpha, message["caption"]))
   
    f_name = f'{datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")}__{message["photo"][0]["file_unique_id"]} {s} .jpg'
    p_name = f'photo_{message["from"]["first_name"]}'
    print(message)
    if not (os.path.exists(p_name)):
        os.mkdir(p_name)
    await message.photo[-1].download(f'{p_name}/{f_name}') 
    await message.reply("Media") 
    
@dp.message_handler()    
async def echo_message(message: types.Message):       
    print("ALL")   
    await message.reply("All") 


if __name__ == "__main__":
    print("start")
    executor.start_polling(dp)
    #get_cours()
    #get_weather("Барнаул",WEA_KEY)