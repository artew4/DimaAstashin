import matplotlib.pyplot as plt


#V = S / T

def time(v):
    #Зависимость T от V
    s = []
    t = []
    for i in range(1, 11):
        s.append(i)
        ti = i / v
        t.append(ti)
    return t, s


func1 = time(1)
plt.plot(func1[0], func1[1], color='red')
func2 = time(2)
plt.plot(func2[0], func2[1], color='green')
func3 = time(4)
plt.plot(func3[0], func3[1], color='purple')
plt.legend(['v= 1', 'v = 2', 'v = 4'])
plt.text(2.1, 1, 'Чем больше v, тем меньше наклон к оси абсцисс', bbox={'facecolor':'yellow','alpha':0.5})
plt.axvline(0)
plt.axhline(0)
plt.xlabel('time')
plt.ylabel('space')
plt.show()
# plt.axline[func1[0], func1[1]]