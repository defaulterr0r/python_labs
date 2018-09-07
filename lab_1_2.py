"""
2. Дан произвольный список, содержащий и строки и числа.
Вариант 4. Выведите все нечетные элементы в одной строке.
"""
# Генерация включена. ctrl + R


import string
import random


def run():
    l = [random.choice(string.digits + string.ascii_letters) for i in range(random.randint(30, 40))]
    print(l)
    l = [i for i in l if (i.isdigit() and (int(i) % 2 == 1))]
    print(''.join(l))
