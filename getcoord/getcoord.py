import pandas as pd
import requests
import json

def get_coords(text):##Функция делает запрос в поиске по организациям
  request = requests.get("https://search-maps.yandex.ru/v1/?text="\
                         +text+"&lang=ru_RU&results=100&\
                        apikey=YOUR_API_KEY")
  place = json.loads(request.content)
  return place
