import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def puasson(x, mu, sig):
    return np.power(mu, x) * np.exp(-mu) / scipy.special.factorial(x)

first = [36, 38, 30, 49, 26, 45, 46, 44, 32, 39, 43, 47, 42,
         42, 44, 33, 43, 29, 41, 41, 40, 32, 34, 41, 39, 39,
         38, 45, 35, 47, 48, 49, 44, 36, 24, 47, 42, 32, 36,
         35, 38, 33, 34, 52, 32, 38, 34, 52, 32, 38, 34, 34,
         31, 34, 40, 39, 43, 26, 30, 31, 49, 35, 35, 30, 28,
         47, 44, 43, 40, 43, 29, 35, 41, 36, 37, 29, 45, 43,
         34, 39, 42, 40, 39, 26, 35, 37, 40, 42, 43, 37, 32,
         42, 41, 35, 35, 35, 39, 41, 35, 38, 33]
second = [70, 55, 58, 60, 61, 68, 68, 46, 59, 72, 60, 66,
          51, 81, 52, 60, 52, 65, 55, 51, 69, 59, 51, 62,
          50, 52, 66, 61, 60, 54, 55, 56, 57, 62, 68, 59,
          57, 65, 64, 65, 62, 65, 54, 55, 55, 58, 61, 60,
          75, 60, 61, 63, 54, 68, 53, 59, 68, 65, 80, 69,
          50, 60, 57, 60, 70, 54, 64, 62, 60, 61, 62, 70,
          72, 54, 74, 63, 66, 59, 50, 73, 71, 68, 53, 64,
          51, 63, 64, 66, 52, 61, 51, 73, 54, 70, 52, 60,
          54, 64, 55, 55]

first = np.array(first)
second = np.array(second)


f_fr = np.sum(first) / len(first)
f_sn = np.sum(second) / len(second)
print(f_fr, f_sn)
print(first, second)

first_count = np.zeros(100)
second_count = np.zeros(100)

dict1 = {i:first.count(i) for i in range(min(first),max(first))+1)}
dict2 = {i:second.count(i) for i in range(min(second),max(second)+1)}
sum_a, sum_b = 0, 0

for i in range(len(first_count)):
    sum_a += first_count[i]
    first_count[i] = sum_a
for i in range(len(second_count)):
    sum_b += second_count[i]
    second_count[i] = sum_b

x = np.arange(0, 100)
print(first_count, second_count)

plt.plot(x, first_count/100, second_count/100)
plt.plot(x, puasson(x, f_fr, np.sqrt(f_fr)))
plt.plot(x, puasson(x, f_sn, np.sqrt(f_sn)))


#plt.hist(first, bins=np.arange(min(first), max(second)))
#plt.hist(second, bins=np.arange(min(first), max(second)))
plt.axis([min(first), max(second), 0, 1])
plt.xlabel('x', color='black')
plt.ylabel('F(x)',color='black')
plt.grid(True)
plt.title("Эмпирическая функция распределения выборки")
plt.show()
