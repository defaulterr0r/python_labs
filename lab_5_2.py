"""
2. Пусть дан файл students.csv, в котором содержится информация о студентах
    Считайте информацию из файла в структуру: [[No, ФИО, Возраст,
    Группа],[No, ФИО, Возраст, Группа],[No, ФИО, Возраст, Группа]] (список списков).

Вариант4. Выведите информацию о студентах, в возрасте старше 22 лет.
"""

import csv


def run():
    # Чтения файла CSV и формирование списка списков
    def csv_reader(file_obj):
        reader = csv.reader(file_obj, delimiter=';')

        out_list = []
        for row in reader:
            out_list.append(row)

        return out_list

    csv_path = '/Users/nidh0gg/Desktop/keklul'
    with open(csv_path, 'r') as file:
        group_list = csv_reader(file)

        # Вывод студентов старше 22 лет
        for i in group_list:
            if int(i[2]) > 22:
                print(' '.join(i))
