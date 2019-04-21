import re

#Читаем текст из файла
with open ("text.txt","r") as f:
    text=f.read()
    print(text)

#Разбиваем на отдельные предложения
list=re.split("\. ",text)

#Выбираем слова, длинной более 4 символов
l1=re.findall("\w{4,}",text)

freq={}
#считаем частоту повторения каждого слова, для этого создаем словарь с ключами - слова, и значениями - количеством
#вхождения

for n in l1:
    i=freq.get(n)
    if i:
        freq[n]+=1
    else:
        freq[n]=1

maximum=0
#Находим максимальное количество вхождений
for i in freq:
    maximum=freq[i] if maximum<freq[i] else maximum

print ("Максимальное число повторений - {}. Перечень слов, длинной от 4 и более".format(maximum))
#печатаем все ключи из словаря со значением с максимальным числом повторений
for n in freq:
    if freq[n]==maximum:
        print(n)



#Отберите все ссылки
sites = re.findall("\S+\.ru/?\w*",text)
print ("Адреса ")
print(sites)

#5. Ссылки на страницы какого домена встречаются чаще всего?

#Отбираем домены из текста
domens=re.findall("[^\. ]+\.ru",text)
print ("Домены ")
print(domens)

#находим наиболее частый домен без учета регистра букв
freq.clear()

for n in domens:
    n1=n.lower()
    i=freq.get(n1)
    if i:
        freq[n1]+=1
    else:
        freq[n1]=1

maximum=0
#Находим максимальное количество вхождений
for i in freq:
    maximum=freq[i] if maximum<freq[i] else maximum

print ("Самый частоупоминаемый домен без учета регистра ")
for n in freq:
    if freq[n]==maximum:
        print(n)


#Замените все ссылки на текст «Ссылка отобразится после регистрации».
print ("Заменяем ссылки на заглушку - текст ")
print(re.sub("\S+\.ru/?\w*","Ссылка отобразится после регистрации",text))