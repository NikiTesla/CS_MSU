"""
    ф-я solution Ищет корень функции на отрезке.
    Находит первый наименьший корень на участке, так как фиксирует только первое вхождение.
    Использует индексы массивов из numpy. Работает не с координатами напрямую, а с индексами массива координат.

    ф-я solutions ищет все корни на отрезке.
    Использует близость к нулю значения функции, ставит в соответствие ей значение х.
    Пробегает весь массив.
"""

import numpy as np
import matplotlib.pyplot as plt


def solution(x, y):
    a, b = 0, len(x)
    while b - a > 2:
        c = (b + a) // 2
        if y[a] * y[c] < 0:
            b = c
        else:
            a = c

    return x[a]


def solutions(x, y):
    list = []
    for i in range(len(y) - 1):
        if y[i] > - eps / 2 and y[i] < eps / 2:
            list.append(x[i]) 

    return list


a, b = float(input("Enter a: ")), float(input("Enter b: "))
eps = 0.01

x = np.arange(a, b, eps)
y = np.sin(x)

print(solution(x, y))
print(solutions(x, y))