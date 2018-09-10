"""
3. Сгенерируйте и выведите:
Вариант 4. Случайную строку, состоящую из 8 символов и содержащую цифры и буквы.
            Строка должна содержать хотя бы одну цифру.
"""


import string
import random


def run():
    s = ''
    temp = string.ascii_letters + string.digits

    for i in range(8):
        s += random.choice(temp)

    if s.isalpha():
        param = random.randint(0, 7)
        s = s[:param] + random.choice(string.digits) + s[param + 1:]

    print(s, len(s))
