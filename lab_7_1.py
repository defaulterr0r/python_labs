"""
1. Пусть дан словарь. Посчитайте и выведите сколько в словаре ключей.
"""

import random

temp = {i:i**2 for i in range(random.randint(10, 20))}
print(temp)
print("Кол-во ключей: ", len(temp.keys()))