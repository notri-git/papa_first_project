import requests
from config import API_KEY


def weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY
    }

    try:
        response = requests.get(url, params=params)
    except:
        return "Не удалось подключиться к серверу"

    if response.status_code != 200:
        return "Не удалось получить данные о погоде"

    data = response.json()

    temp = data["main"]["temp"] - 273.15
    feels = data["main"]["feels_like"] - 273.15
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    result = (
        "Температура: " + str(round(temp, 1)) + " °C\n"
        "Ощущается как: " + str(round(feels, 1)) + " °C\n"
        "Влажность: " + str(humidity) + " %\n"
        "Ветер: " + str(wind) + " м/с\n"
        "Погода: " + description
    )

    return result