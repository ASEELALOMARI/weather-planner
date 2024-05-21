#The open-meteo website does not accept city names for search. 
#This data set to converts the city name to the variables required for search, 
#which are longitude, latitude, and time zone.

#You can increase the data as needed

city_data = {
    'New York': {'latitude': 40.7128, 'longitude': -74.0060, 'timezone': 'America/New_York'},
    'London': {'latitude': 51.5074, 'longitude': -0.1278, 'timezone': 'Europe/London'},
    'Tokyo': {'latitude': 35.6895, 'longitude': 139.6917, 'timezone': 'Asia/Tokyo'},
    'Moscow': {'latitude': 55.7558, 'longitude': 37.6176, 'timezone': 'Europe/Moscow'},
    'Dubai': {'latitude': 25.2769, 'longitude': 55.2963, 'timezone': 'Asia/Dubai'},
    'Riyadh': {'latitude': 24.7136, 'longitude': 46.6753, 'timezone': 'Asia/Riyadh'},
    'Qassim': {'latitude': 26.1960, 'longitude': 43.0815, 'timezone': 'Asia/Riyadh'},
    'Mecca': {'latitude': 21.3891, 'longitude': 39.8579, 'timezone': 'Asia/Riyadh'},
    'Medina': {'latitude': 24.5247, 'longitude': 39.5692, 'timezone': 'Asia/Riyadh'},
    'Cairo': {'latitude': 30.0444, 'longitude': 31.2357, 'timezone': 'Africa/Cairo'},
    'Amman': {'latitude': 31.9522, 'longitude': 35.2332, 'timezone': 'Asia/Amman'},
    'Kuwait': {'latitude': 29.3759, 'longitude': 47.9774, 'timezone': 'Asia/Kuwait'},
    'Doha': {'latitude': 25.2769, 'longitude': 51.5200, 'timezone': 'Asia/Qatar'},
    'Abha': {'latitude': 18.2306, 'longitude': 42.5001, 'timezone': 'Asia/Riyadh'},
    'Seoul': {'latitude': 37.5665, 'longitude': 126.9780, 'timezone': 'Asia/Seoul'},
    'Shanghai': {'latitude': 31.2304, 'longitude': 121.4737, 'timezone': 'Asia/Shanghai'},
    'Beijing': {'latitude': 39.9042, 'longitude': 116.4074, 'timezone': 'Asia/Shanghai'},
    'Cambridge Bay': {'latitude': 69.1139, 'longitude': -105.0524, 'timezone': 'America/Edmonton'},
}