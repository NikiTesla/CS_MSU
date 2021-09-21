from math import pi
sum, si = 1, 1

x = float(input("Enter x: "))
eps = float(input("Enter eps: "))
n = int(input("Enter n: "))

for i in range(n):
    print(si)
    si *= -1 * x**2 / ((2 * i + 1) * (2 * i + 2))
    sum += si

    if si < eps and si > 0 or si > -eps and si < 0:
        break

print("Result: ", sum)

