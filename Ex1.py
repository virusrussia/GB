#1. Получить количество учеников с сайта geekbrains.ru:

#a) при помощи регулярных выражений,

import re
from bs4 import BeautifulSoup as BS

with open ("GeekBrains - образовательный портал.html","r") as f:
    text=f.read()

peoples = re.findall("total-users\">(Нас уже .*?)</span>",text)

print(peoples)

#<div class="col"><span class="total-users">Нас уже 3 734 172 человек</span>
#<a class="btn sign-in" href="/login">Войти</a></div></div>

#b) при помощи библиотеки BeautifulSoup.

Soup=BS(text, "html.parser")

li=Soup.find_all("div")


for n in li:
   if n.get("class","")=="col":
       print(n.get("span",""))