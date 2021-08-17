import requests as req


def format_response(weather_json):
    #format json data
    try:
        city_name = weather_json['name']
        condition = weather_json['weather'][0]['description']
        temperature = weather_json['main']['temp']
        icon_name = weather_json['weather'][0]['icon']
        weather_report = 'City: %s \n Condition: %s \n Temperature (°F): %s'% (city_name, condition, temperature)

    except:
        weather_report = 'Ooooops!, Failed to get informations'
        icon_name = ''
    return (weather_report, icon_name)
        

def weather_info(city_name):
    weather_key = '31bd7bdf7f2be12124b4ca67e1fa7cad'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city_name, 'units': 'imperial'}
    res = req.get(url, params)
    weather_json = res.json()
    weather_report = format_response(weather_json)
    return weather_report