from from_pdf import lab_1_2, lab_4_2, lab_1_3, lab_3_1, lab_3_4, lab_4_1, lab_5_1, lab_5_2, lab_2_3, lab_2_2
from prettytable import PrettyTable


def launch():
    table = PrettyTable(["код", "модуль"])
    table.add_row(["0", "Лабораторная работа №1. Задание №2"])
    table.add_row(["1", "Лабораторная работа №1. Задание №3"])
    table.add_row(["2", "Лабораторная работа №2. Задание №2"])
    table.add_row(["3", "Лабораторная работа №2. Задание №3"])
    table.add_row(["4", "Лабораторная работа №3. Задание №1"])
    table.add_row(["5", "Лабораторная работа №3. Задание №4"])
    table.add_row(["6", "Лабораторная работа №4. Задание №1"])
    table.add_row(["7", "Лабораторная работа №4. Задание №2"])
    table.add_row(["8", "Лабораторная работа №5. Задание №1"])
    table.add_row(["9", "Лабораторная работа №5. Задание №2"])
    print(table)


def parser(arg: str):
    fun = {'0': lab_1_2.run, '1': lab_1_3.run, '2': lab_2_2.run, '3': lab_2_3.run, '4': lab_3_1.run,
           '5': lab_3_4.run, '6': lab_4_1.run, '7': lab_4_2.run, '8': lab_5_1.run, '9': lab_5_2.run}

    if arg in fun.keys():
        fun[arg].__call__()
    else:
        print("Некорректный аргумент!")


if __name__ == '__main__':
    launch()
    while True:
        response = input("Выберите нужный вариант: ")
        parser(response)

        restart = input('Вы хотите продолжить? Y/N\n')
        if restart == "Y":
            continue
        elif restart == "N":
            break
        else:
            print("Некорректный аргумент")
            continue
