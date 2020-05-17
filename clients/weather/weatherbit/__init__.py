import requests

import clients.weather.models as models

def get_weather(city):
    # https://www.weatherbit.io/api/weather-current
    api_key = 'dc0c2cf4677442d3b043e48a95e0c799'
    response = requests.get(
        'https://api.weatherbit.io/v2.0/current',
        params={
            'city': city,
            'key': api_key
        }

    )

    data = response.json()
    print(data)

    return models.Weather(data['data'][0]['app_temp'] + 273.15, data['data'][0]['wind_spd'] )
