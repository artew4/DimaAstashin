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
        d = k * x[i]
        print(d)
        y.append(d)
    print(y)
    global xy1
    xy1 = (x[1], y[1])
    global xy2
    xy2 = (x[2], y[2])
fun(1)
plt.axline(xy1, xy2, color='red')
fun(-1)
plt.axline(xy1, xy2, color='red')
fun(-2)
plt.axline(xy1, xy2, color='purple')
fun(-0.5)
plt.axline(xy1, xy2, color='green')
plt.title(f'y = k*x')
plt.legend([f'k=1','k=-1', f'k=-2', 'k=-0.5'])
plt.text(-5, 9, 'Чем больше k, тем меньше наклон к оси x', bbox={'facecolor':'yellow','alpha':1})
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.axvline(0)
plt.axhline(0)
plt.show()

# plt.plot(x, y, color='r')
# plt.show()