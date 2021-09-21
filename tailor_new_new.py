sk, i, sum  = 1, 0, 1
eps = float(input("Enter eps:"))


def element(x):
    global sk, sum, i
    print(sk)

    sk *= -1 * x**2 / ((2 * i + 1) * (2 * i + 2))
    sum += sk
    i += 1

    if sk > eps and sk > 0 or sk < eps and sk < 0:
        element(x)


element(float(input("Enter x: ")))
print("Result: ", sum)