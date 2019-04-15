#1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:

#my_favourite_group = {
#‘name’: ‘Г.М.О.’,
#‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
#‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
#{‘name’: ‘Шапито’,‘year’: 2014}]}
#С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import pickle, json

my_favourite_group = {
    "name": "The Prodigy",
    "tracks": ["Smack my bitch up", "Poison"],
    "Albums": [{"name": "The fat of the land","year": 1996},
    {"name": "Expirience for the jilted generation","year": 1992}]}


print("Pickle:")
print(pickle._dumps(my_favourite_group))

print("json:")
print(json.dumps(my_favourite_group))

with open("Pdata.dat","wb") as f:
    pickle.dump(my_favourite_group,f)

print("Pickle load:")
with open("Pdata.dat","rb") as f:
    print(pickle.load(f))

with open("Jdata.dat","w",encoding="utf-8") as f:
    json.dump(my_favourite_group,f)

print("Json load:")
with open("Jdata.dat", "r",encoding="utf-8") as f:
    print(json.load(f))
