# import os
#
# import requests
# from dotenv import load_dotenv
#
# load_dotenv()
#
# def get_temperature(city):
#     url='https://api.openweathermap.org/data/2.5/weather'
#     appid=os.getenv('APIKEY')
#     response=requests.get(url, params={
#         'q': city,
#         'units': 'metric',
#         'appid': appid
#     })
#     return response.json()
#
#####################################################################################


# NEW TG BOT'S API

import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_temperature(long, lat):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
        'lon': long,
        'lat': lat,
        'units': 'metric',
        'appid': os.getenv('APIKEY')
    }
    response = requests.get(url, params=params)
    return response.json()


# def get_address_using_location(lon, lat):
#     url = "https://geocode-maps.yandex.ru/1.x/"
#     params = {
#         "apikey": "f3d55107-23fa-41bf-88c4-51b44aaf6781",
#         "geocode": f"{lon},{lat}",
#         "lang": "en",
#         "format": "json"
#     }
#     response = requests.get(url, params=params)
#     data_p = response.json()
#     city = data_p['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
#         'GeocoderMetaData']['Address']['formatted']
#     return city


def get_address_location(lat, lon):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": f"{lat},{lon}"}

    headers = {
        "X-RapidAPI-Key": "8afc2011abmsh7411ffeb2050b59p1e192fjsn4cf62169cbab",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    country = data['location']['country']
    city = data['location']['name']
    return f"{country} {city}"

