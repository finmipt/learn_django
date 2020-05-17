from django.http import HttpResponse

import clients.weather.weatherbit as weather


def index(request):
    weather_data = weather.get_weather('Moscow')
    return HttpResponse(f'{weather_data.temperature - 273.15} C <br /> {weather_data.wind_speed} m/s')
