# weather_images.py
# To convert the weather description into an appropriate image

#URL data set
weather_images = {
    'Clear sky': {
        'daylight': '../static/img/weather/sun.png',
        'night': '../static/img/weather/moon.png',
    },
    'Mainly clear': {
        'daylight': '../static/img/weather/clouds-sun.png',
        'night': '../static/img/weather/clouds-moon.png',
    },
    'Fog': '../static/img/weather/fog.png',
    'Drizzle': '../static/img/weather/light-rain.png',
    'Freezing Drizzle': '../static/img/weather/light-rain.png',
    'Rain': '../static/img/weather/heavy-rain.png',
    'Freezing Rain': '../static/img/weather/heavy-rain.png',
    'Snowfall': '../static/img/weather/snow.png',
    'Snow grains': '../static/img/weather/snow.png',
    'Rain showers': '../static/img/weather/heavy-rain.png',
    'Snow showers': '../static/img/weather/heavy-rain.png',
    'Thunderstorm': '../static/img/weather/storm.png',
    'Unknown': '../static/img/weather/sun.png',
}


def get_image_url(weather_condition, is_day):
    # Check if the weather condition has separate URLs for day and night
    if weather_condition in weather_images and isinstance(weather_images[weather_condition], dict):
        if is_day == 'daylight': 
            return weather_images[weather_condition].get('daylight', '/static/unknown.png')
        elif is_day == 'night':
            return weather_images[weather_condition].get('night', '/static/unknown.png')
    else:
        # Use the default image URL for conditions without separate day/night URLs
        return weather_images.get(weather_condition, '/static/unknown.png')

