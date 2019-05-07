#1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests, json   

city=input("Введите название города: ")

resp=requests.get(f"https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{city}%20в%20Цюрих")

iata=json.loads(resp.text)

print("Код IATA для введенного города - ",iata["origin"]["iata"])