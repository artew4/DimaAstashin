import matplotlib.pyplot as plt


# T = S / V
def time(s):
    # Зависимость T от S
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

# Делаем оформление
plt.title("Зависимость T от S")
plt.xlabel('time')
plt.ylabel('velocity')
plt.text(0.8, 6, 'Чем больше s, тем выше расположение гиперболы', bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axvline(0)
plt.axhline(0)
plt.axline((1.0, 0.0), (1.0, 2.0), linestyle=':')
plt.plot(1, 1, 'yo')
plt.plot(1, 4, 'yo')
plt.plot(1, 2, 'yo')
plt.text(1.1, 0.5, "T=const, S↑ V↑", bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axline((0.0, 2.0), (1.0, 2.0), linestyle=':')
plt.plot(0.5, 2, 'go')
plt.plot(1, 2, 'go')
plt.plot(2, 2, 'go')
plt.text(2.1, 2.5, "V=const, S↑ T↑", bbox={'facecolor': 'green', 'alpha': 0.5})
plt.text(2.1, 3.5, "S=const, T↑ V↓", bbox={'facecolor': 'red', 'alpha': 0.5})

plt.show()
