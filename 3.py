""""
3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:

name — строка, полученная от пользователя,
health = 100,
damage = 50.
Поэкспериментируйте с значениями урона и жизней по желанию.

Теперь надо создать функцию attack(person1, person2).

Примечание: имена аргументов можете указать свои.
Функция в качестве аргумента будет принимать атакующего и атакуемого.

В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна
 сама работать со словарями и изменять их значения.
 """

import random

def attack (person1, person2):
    person1["health"]-=person2.get("damage")



pname = input("Введите имя player: ")
ename = input("Введите имя enemy: ")

player= {"name": pname, "health":100, "damage":random.randint(1,25)}
enemy= {"name": pname, "health":100, "damage":random.randint(1,25)}



attack(enemy, player)

print(enemy.get("health"))