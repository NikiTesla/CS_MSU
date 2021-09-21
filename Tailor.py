from math import *

elements = []


def element(x, n):
    return (pow(-1, n-1) * pow(x, 2*n - 2)) / factorial(2*n - 2)


def tailor(x, n):
    result = 0

    for i in range(1, n + 1):
        result += element(x, i)
        elements.append(element(x, i))

    return result

print("Result: ", tailor(float(input("Enter x: ")), int(input("Enter n: "))))

for i in elements:
    print(i)