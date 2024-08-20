import matplotlib.pyplot as plt


#T = S / V
def time(s):
    #Зависимость T от S
    v = []
    t = []
    for i in range(1, 11):
        v.append(i)
        ti = s / i
        t.append(ti)
    return t, v


func1 = time(1)
plt.plot(func1[0], func1[1], color='red')
func2 = time(2)
plt.plot(func2[0], func2[1], color='green')
func3 = time(4)
plt.plot(func3[0], func3[1], color='purple')
plt.legend(['s = 1', 's = 2', 's = 4'])
plt.text(1, 5, 'Чем больше s, тем больше длина параболы', bbox={'facecolor':'yellow','alpha':0.5})
plt.axvline(0)
plt.axhline(0)
plt.xlabel('time')
plt.ylabel('velocity')
plt.show()