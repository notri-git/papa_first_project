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
        print("Не удалось подключиться к серверу")
        return

    if response.status_code != 200:
        print("Не удалось получить данные о погоде")
        return

    data = response.json()
    temp = data["main"]["temp"] - 273.15
    feels = data["main"]["feels_like"] - 273.15
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    print("Температура:", round(temp, 1), "°C")
    print("Ощущается как:", round(feels, 1), "°C")
    print("Влажность:", humidity, "%")
    print("Ветер:", wind, "м/с")
    print("Погода:", description)