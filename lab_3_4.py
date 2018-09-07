"""
4. Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов.
"""

import random
import string


def run():
    s = ''
    for i in range(random.randint(40, 60)):
        s += random.choice(string.ascii_lowercase + ' ')

    print(s)
    print("кол-во слов: %i" % ((s.count(' ') + 1) if s.count(' ') else 0))
    print("кол-во символов включая пробельный: %i" % (len(s)))