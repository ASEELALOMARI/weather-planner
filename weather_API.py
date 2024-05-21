import openmeteo_requests
import requests_cache
import pandas as pd

from retry_requests import retry
from datetime import datetime



#convert the URL variable to readable one :

#Converting the weather code numbers into an understandable phrase if code is 0 then it's mean Clear sky and so on.
def get_weather_description(code):
    code_mapping = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Mainly clear",
        3: "Mainly clear",
        45: "Fog",
        48: "Fog",
        51: "Drizzle",
        53: "Drizzle",
        55: "Drizzle",
        56: "Freezing Drizzle",
        57: "Freezing Drizzle",
        61: "Rain",
        63: "Rain",
        65: "Rain",
        66: "Freezing Rain",
        67: "Freezing Rain",
        71: "Snowfall",
        73: "Snowfall",
        75: "Snowfall",
        77: "Snow grains",
        80: "Rain showers",
        81: "Rain showers",
        82: "Rain showers",
        85: "Snow showers",
        86: "Snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm",
        99: "Thunderstorm",
    }

    return code_mapping.get(code, "Unknown")

#convert the time to human readable time
def current_time(timestamp):
    readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d / %H:%M')

    return readable_time

#convert day value form 1 if the current time step has daylight, 0 at night.
def is_day(day):
    if (day == 1):
        day_is ='daylight'
    else :
        day_is = 'night'

    return day_is






#get wether info from open-meteo API [code form open-meteo documentation]
def get_weather_data(lat,long,zone):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude":long,
        "current": ["temperature_2m", "is_day", "precipitation", "weather_code", "wind_speed_10m"],
        "timezone": zone,
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_is_day = current.Variables(1).Value()
    current_precipitation = current.Variables(2).Value()
    current_weather_code = current.Variables(3).Value()
    current_wind_speed_10m = current.Variables(4).Value()


    #return value of the functions
    Time = current_time(current.Time())
    Temp = int(current_temperature_2m)
    Day = is_day(int(current_is_day))
    Weather = get_weather_description(int(current_weather_code))
    Precipitation = int(current_precipitation)
    Wind = int(current_wind_speed_10m)

    return Time, Temp, Day, Weather, Precipitation, Wind
