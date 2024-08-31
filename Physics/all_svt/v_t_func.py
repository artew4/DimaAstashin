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

# Делаем оформление
plt.title("Зависимость V от T")
plt.xlabel('velocity')
plt.ylabel('space')
plt.axline((1.0, 0.0), (1.0, 2.0), linestyle=':')
plt.plot(1, 1, 'yo')
plt.plot(1, 4, 'yo')
plt.plot(1, 2, 'yo')
plt.text(4, 2, "V=const, T↑ S↑", bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axline((0.0, 2.0), (1.0, 2.0), linestyle=':')
plt.plot(0.5, 2, 'go')
plt.plot(1, 2, 'go')
plt.plot(2, 2, 'go')
plt.text(4.5, 3, "S=const, V↑ T↓", bbox={'facecolor': 'green', 'alpha': 0.5})
plt.text(5.6, 4, "T=const, V↑ S↑", bbox={'facecolor': 'red', 'alpha': 0.5})
plt.text(2.1, 1, 'Чем больше t, тем меньше наклон к оси абсцисс', bbox={'facecolor':'yellow','alpha':0.5})
plt.axvline(0)
plt.axhline(0)

plt.show()
# plt.axline[func1[0], func1[1]]