import matplotlib.pyplot as plt


# V = S / T

def velocity(s):
    # Зависимость V от S
    t = []
    v = []
    for i in range(1, 11):
        t.append(i)
        vi = s / i
        v.append(vi)
    return v, t


func1 = velocity(1)
plt.plot(func1[0], func1[1], color='red')
func2 = velocity(2)
plt.plot(func2[0], func2[1], color='green')
func3 = velocity(4)
plt.plot(func3[0], func3[1], color='purple')
plt.legend(['S = 1', 'S = 2', 'S = 4'])

# Делаем оформление
plt.title("1. Зависимость V от S")
plt.xlabel('velocity')
plt.ylabel('time')
plt.text(0.8, 6, 'Чем больше s, тем выше расположение гиперболы', bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axvline(0)
plt.axhline(0)
plt.axline((1, 0), (1, 2), linestyle=':')
plt.plot(1, 1, 'yo')
plt.plot(1, 4, 'yo')
plt.plot(1, 2, 'yo')
plt.text(1.1, 0.5, "V=const, S↑ T↑", bbox={'facecolor': 'yellow', 'alpha': 0.5})
plt.axline((0, 2), (1, 2), linestyle=':')
plt.plot(0.5, 2, 'go')
plt.plot(1, 2, 'go')
plt.plot(2, 2, 'go')
plt.text(2.1, 2.5, "T=const, S↑ V↑", bbox={'facecolor': 'green', 'alpha': 0.5})
plt.text(2.1, 3.5, "S=const, T↑ V↓", bbox={'facecolor': 'red', 'alpha': 0.5})

plt.show()
