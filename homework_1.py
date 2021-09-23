from math import pi


def sum(x, eps, n):
    """
        Считает косинус с помощью разложения в ряд тейлора.
    
        Считает n-й член ряда через предыдущий.
        Суммирует их и выводит результат.
        Считает, пока член не станет меньше eps,
        либо до n-го члена по порядку.
    """
    sum, si = 1, 1
    for i in range(n):
        print(si)
        si *= -1 * x**2 / ((2 * i + 1) * (2 * i + 2))
        sum += si

        if si < eps and si > 0 or si > -eps and si < 0:
            break
    
    return sum


x = float(input("Enter x: "))
eps = float(input("Enter eps: "))
n = int(input("Enter n: "))


print("Result: ", sum(x, eps, n))

