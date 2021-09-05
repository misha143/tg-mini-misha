import time
import requests
import telegram

tokentg = '1905742443:AAE5wT7SEaVIA3LSDTZeJzbihlmvDhUYvZA'
tgid = '386589423'


def weather():
    url = f'http://wttr.in/Пермь'
    weather_parameters = {
        'format': 3,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

bot = telegram.Bot(token=tokentg)

while True:
    bot.send_message(tgid, f'{weather()}')
    time.sleep(60*30)
