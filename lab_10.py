matr = [
    [int(x) for x in '26351732'],
    [int(x) for x in '87654321'],
    [int(x) for x in '23456789'],
    [int(x) for x in '98765432'],
    [int(x) for x in '13579753'],
    [int(x) for x in '31532657'],
    [int(x) for x in '17597315'],
    [int(x) for x in '26351732'],
]


def summ(param):
    val = 0
    for i in param:
        for x in i:
            val += x

    return val
