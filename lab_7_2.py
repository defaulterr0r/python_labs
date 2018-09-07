"""
2. Пусть дан файл students.csv, в котором содержится информация о студентах
    Считайте информацию из файла в структуру: {No: [ФИО, Возраст,
    Группа], No: [....], No: [....]} (словарь, где ключи – это порядковые номера студентов).

Вариант 4. Выведите информацию о студентах, в возрасте старше 22 лет.
"""

import csv


# Чтения файла CSV и формирование списка списков
def csv_reader(file_obj):
    reader = csv.reader(file_obj, delimiter=';')

    out_dict = {}
    for row in reader:
        out_dict[row[0]] = row[1:]

    return out_dict


csv_path = '/Users/nidh0gg/Desktop/keklul'
with open(csv_path, 'r') as file:
    group_list = csv_reader(file)

    # Вывод студентов старше 22 лет
    for val in group_list.values():
        if int(val[1]) > 22:
            print(' '.join(val))
