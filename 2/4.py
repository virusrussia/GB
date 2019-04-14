""""
4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)

Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor

Следовательно, у вас должно быть 2 функции:

1. Наносит урон. Это улучшенная версия функции из задачи 3.

2. Вычисляет урон по отношению к броне.
 """

import random

def attack (person1, person2):

    def defence (person1, person2):
        print ("Отношение атаки к защите: ", person2["damage"]/person1["armor"])
        return person2["damage"]/person1["armor"]

    person1["health"]-=defence(person1, person2)



pname = input("Введите имя player: ")
ename = input("Введите имя enemy: ")

player= {"name": pname, "health":100, "damage":random.randint(1,25), "armor":random.randint(10,15)/10}
enemy= {"name": pname, "health":100, "damage":random.randint(1,25), "armor":random.randint(10,15)/10}


print(f"У игрока {enemy['name']} сила удара {enemy['damage']}, у игрока {player['name']} уровень защиты {player['armor']}")

attack(player, enemy)

print(player.get("health"))