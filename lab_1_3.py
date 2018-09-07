"""
3. Дан произвольный список, содержащий только числа.
Вариант 4. Выведите результат умножения всех чисел меньше 10.
"""
# Генерация включена. ctrl + R


import random


def run():
    # Задание списка
    l = []
    for i in range(random.randint(10, 20)):
        l.append(random.randint(-5, 20))

    # Вывод
    print(l)
    fin = 1
    for i in l:
        if i < 10:
            fin *= i

    print(fin)
