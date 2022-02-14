import requests
import json
from keys import OPEN_WEATHER_MAP_API_KEY

api_key = OPEN_WEATHER_MAP_API_KEY
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

latitude = 27.218247
longitude = 78.272821

complete_url = base_url + f'lat={latitude}' + f'&lon={longitude}' + f'&appid={api_key}' + f'&units=metric'
session = requests.Session()
response = session.get(complete_url)

# print(response)
print(response.status_code, type(response.status_code))
x = response.json()
print(x)

