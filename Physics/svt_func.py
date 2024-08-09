import matplotlib.pyplot as plt
#import numpy as np
# s = v * t
# Пример 1 Зависимость пути от скорости
# S(v) = v * t




#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ДЗ - исследовать y = k * x
# построить графики

# для построения функции - берем значение Х
# и рассчитываем У
# функция 1: k = 2 -> y = 2 * x
# 1 точка) x = 0 -> y = 2 * 0 = 0
# 2 точка) x = 1 -> y = 2 * 1 = 2
# 3 точка) x = 2 -> y = 2 * 2 = 4
# 4 точка) x = 3 -> y = 2 * 3 = 6
#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [0, 2, 4, 6, ...]
# построение функции:
# plt.plot(x, y, color='r', label='y = k*x, k = 2')
# plt.show()

#k равен 3 положительных
#k равен 3 отрицательных
#k равен 3 положительных дробных(float)
#k равен 3 отрицательных дробных(float)
#https://matplotlib.org/stable/users/explain/quick_start.html


def fun(k):
    x = []
    y = []
    for i in range(11):
        x.append(i)
    
    for i in range(11):
        s = x[i]
        d = k * s
        print(d)
        y.append(d)
    plt.plot(x, y, color='r')
    plt.ylabel(f'y = k*x, k = {k}')
    plt.grid(color='b')
    plt.xlim(-10, 10)
    plt.ylim(-10,10)
    plt.show()
fun(-3.4)
# plt.plot(x, y, color='r')
# plt.show()