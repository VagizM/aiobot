import requests
from pprint import pprint
from auth import WEA_KEY
import time
ARR =["С","ССВ","СВ","ВСВ","В","ВЮВ", "ЮВ", "ЮЮВ","Ю","ЮЮЗ","ЮЗ","ЗЮЗ","З","ЗСЗ","СЗ","ССЗ"]
DESK={2:"Гроза",3:"Морось",5:"Дождь",6:"Снег",7:"Туман",8:"Облачно"}
'''
FULL_DESK={200:"гроза с небольшим дождем",201:"гроза с дождем",202:"гроза с проливным дождем",211:"гроза",212:"",221:"",230:"",231:"",232:"",
           200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",200:"",
           200:"",200:"",200:"",200:"",200:"",}
'''
def degToCompass(num):
    val=int((num/22.5)+.5)
    return (ARR[val % 16])
    
def codToDescripnion(cod):
    if cod ==800: return "Безоблачно"    
    return DESK[cod//100]
    
    
def get_weather(city_name,API_key):    
    st =f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=Metric'    
    try:        
        data = requests.get(st).json()
    except Exception as e: 
        print("ERR",e)
    pprint(data)
    if data["cod"]==200:    
        city = data["name"]
        temp = data["main"]["temp"]
        desk = data["weather"][0]["description"]
        #print("RESP",city,temp,desk)
        cardinal = degToCompass(data["wind"]["deg"])
        description = codToDescripnion(int(data["weather"][0]["id"]))
        return f'Сейчас в <b>{time.strftime("%H.%M",time.localtime())}</b>, в городе {data["name"]} температура <b>{data["main"]["temp"]}°С</b> , влажность {data["main"]["humidity"]}, ветер {cardinal} скорость {data["wind"]["speed"]} м/с, {description}'
        #{} Сейчас в {время} в городе {город} температура {}°С , влажность {}, ветер {град} {ветер} м/с, {codToDescripnion({})}
        #f'В городе {city} сегодня {temp}*С , {desk}'
    else:
        return f'город не найден'
if __name__ == "__main__":
    print(get_weather("Barnaul",WEA_KEY)) 