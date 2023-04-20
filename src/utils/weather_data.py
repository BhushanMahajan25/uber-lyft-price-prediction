import json
import requests
import pandas as pd
from os import environ as env
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

def weather_information(latitude, longitude):
    '''
    Get weather information of the location
    param : latitude, longitude of a location
    return : weather object with all the required parameters
    '''
    api_key = env.get('OPEN_WEATHER_API_KEY')
    units = "imperial"
    
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units={}&appid={}".\
        format(latitude, longitude, units, api_key)

    response = requests.get(url)
    response_data = json.loads(response.text)
    print("response_data: ", response_data)

    weather_model_parameters_dict = {'location_latitude': latitude, 'location_longitude': longitude}
    weather_model_parameters_dict['temp'] = response_data['main']['temp']
    weather_model_parameters_dict['clouds'] = response_data['clouds']['all'] / 100
    if 'rain' in response_data:
        weather_model_parameters_dict['rain'] = response_data['rain']['1h'] / 25.4
    else:
        weather_model_parameters_dict['rain'] = 0
    weather_model_parameters_dict['pressure'] = response_data['main']['pressure']
    weather_model_parameters_dict['humidity'] = response_data['main']['humidity'] / 100
    weather_model_parameters_dict['wind'] = response_data['wind']['speed']
    weather_model_parameters_dict['id'] = 0

    current_weather_df = pd.DataFrame.from_dict(weather_model_parameters_dict, orient='index')
    current_weather_df = current_weather_df.transpose()
    return current_weather_df