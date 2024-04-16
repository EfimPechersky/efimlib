import requests
import json

def get_coords(text,api_key):##Функция делает запрос в поиске по организациям
  request = requests.get("https://search-maps.yandex.ru/v1/?text="\
                         +text+"&lang=ru_RU&results=100&\
                        apikey="+api_key)
  place = json.loads(request.content)
  return place
