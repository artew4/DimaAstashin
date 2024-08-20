import matplotlib.pyplot as plt


#V = S / T

def velocity(s):
    #Зависимость V от S
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
plt.text(1, 5, 'Чем больше s, тем больше длина параболы', bbox={'facecolor':'yellow','alpha':0.5})
plt.axvline(0)
plt.axhline(0)
plt.xlabel('velocity')
plt.ylabel('time')
plt.show()
# plt.axline[func1[0], func1[1]]