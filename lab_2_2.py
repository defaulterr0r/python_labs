"""
2. Пусть задан список, содержащий строки.
Вариант 4. Выведите все строки, начинающиеся с буквы r.
"""
# Генерация включена. ctrl + R


import random
import string


def run():
    # Задание списка
    l = []
    for i in range(random.randint(15, 20)):
        s = ''
        for x in range(4):
            s += random.choice(string.ascii_lowercase)
        l.append(s)

    # Вывод
    print(l)
    for i in l:
        if i[0] == 'r':
            print(i)
