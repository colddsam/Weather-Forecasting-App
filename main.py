import requests
from datetime import datetime
base__url="http://api.openweathermap.org/data/2.5/weather?"
api__key=open('api__key.txt','r').read()

def kelvin_to_celsius(temp):
    return temp-273.15

def parameters(information):
    longitude=information['coord']['lon']
    latitude=information['coord']['lat']
    enviroment=information['weather'][0]['main']
    max_temp=information['main']['temp_max']
    min_temp=information['main']['temp_min']
    temp=information['main']['temp']
    feels_like=information['main']['feels_like']
    humidity=information['main']['humidity']
    pressure=information['main']['pressure']
    wind_speed=information['wind']['speed']
    clouds=information['clouds']['all']
    sunrise=information['sys']['sunrise']
    sunset=information['sys']['sunset']
    timezone=information['timezone']
    country=information['sys']['country']
    return longitude,latitude,enviroment,max_temp,min_temp,temp,feels_like,humidity,pressure,wind_speed,clouds,sunrise,sunset,timezone,country
def convert_data(request):
    longitude,latitude,enviroment,max_temp,min_temp,temp,feels_like,humidity,pressure,wind_speed,clouds,sunrise,sunset,timezone,country=parameters(request)
    max_temp=kelvin_to_celsius(max_temp)
    min_temp=kelvin_to_celsius(min_temp)
    temp=kelvin_to_celsius(temp)
    feels_like=kelvin_to_celsius(feels_like)
    sunrise=sunrise+timezone
    sunset=sunset+timezone
    sunset=datetime.utcfromtimestamp(sunset)
    sunrise=datetime.utcfromtimestamp(sunrise)
    return str(round(temp)),str(round(max_temp)),str(round(min_temp)),str(round(feels_like)),str(round(humidity)),str(latitude),str(longitude),str(enviroment),str(round(pressure)),str(round(wind_speed)),country,clouds,sunrise,sunset,timezone

def get_information(city):
    url=base__url+"appid="+api__key+"&q="+city
    try:
        request=requests.get(url=url).json()
        return True,convert_data(request=request)
    except:
        return False,False