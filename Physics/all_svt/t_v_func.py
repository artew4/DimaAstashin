import matplotlib.pyplot as plt


# V = S / T

def time(v):
    # Зависимость T от V
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

# Делаем оформление
plt.title("Зависимость T от V")
plt.xlabel('time')
plt.ylabel('space')
plt.axline((1.0, 0.0), (1.0, 2.0), linestyle=':')
plt.plot(1, 1, 'yo')
plt.plot(1, 4, 'yo')
plt.plot(1, 2, 'yo')
plt.text(4, 2, "T=const, V↑ S↑", bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axline((0.0, 2.0), (1.0, 2.0), linestyle=':')
plt.plot(0.5, 2, 'go')
plt.plot(1, 2, 'go')
plt.plot(2, 2, 'go')
plt.text(4.5, 3, "S=const, V↑ T↓", bbox={'facecolor': 'green', 'alpha': 0.5})
plt.text(5.6, 4, "V=const, T↑ S↑", bbox={'facecolor': 'red', 'alpha': 0.5})
plt.text(2.1, 1, 'Чем больше v, тем меньше наклон к оси абсцисс', bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axvline(0)
plt.axhline(0)

plt.show()
