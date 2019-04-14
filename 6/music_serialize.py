#1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:

"""my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}
С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8."""
import pickle
import json

my_favorite_group={"name":"The Prodigy", "traks":["Breathe", "Firestarter"],
                   "Albums":[{"name":"The Prodigy Expirience", "year":1991}, {"name":"The Fat Of The Land", "year":1996}]}

print(pickle.dumps(my_favorite_group))

print(json.dumps(my_favorite_group))