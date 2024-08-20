import matplotlib.pyplot as plt


#V = S / T

def velocity(t):
    #Зависимость V от S
    s = []
    v = []
    for i in range(1, 11):
        s.append(i)
        vi = i / t
        v.append(vi)
    return v, s


func1 = velocity(1)
plt.plot(func1[0], func1[1], color='red')
func2 = velocity(2)
plt.plot(func2[0], func2[1], color='green')
func3 = velocity(4)
plt.plot(func3[0], func3[1], color='purple')
plt.legend(['t = 1', 't = 2', 't = 4'])
plt.text(2.1, 1, 'Чем больше t, тем меньше наклон к оси абсцисс', bbox={'facecolor':'yellow','alpha':0.5})
plt.axvline(0)
plt.axhline(0)
plt.xlabel('velocity')
plt.ylabel('space')
plt.show()
# plt.axline[func1[0], func1[1]]