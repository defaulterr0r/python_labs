"""
2. Пусть дан список из 10 элементов.
Вариант 4. Добавьте 5 новых элементов и оставьте все нечетные элементы.
            Выведите список на экран.
"""

import random


def run():
    l = [random.randint(1, 50) for i in range(10)]
    print("Изначально:\t\t\t", l)

    for i in range(5):
        l.append(random.randint(1, 50))

    print("После добавления:\t", l)

    l = [i for i in l if (i % 2) == 1]
    print("Только нечетные:\t", l)
