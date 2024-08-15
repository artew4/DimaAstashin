import random as rnd


def primer():
    znaki = ('+', '-', '*', '/')
    lst = []
    for i in range(rnd.randint(3, 5)):
        lst.append(rnd.randint(1, 20))
        lst.append(rnd.choice(znaki))
    lst.pop()
    return lst


def counter(lst):
    s = ''
    for i in lst:
        s += str(i)
    s += '='
    print(lst)
    while '*' or '/' in lst:
        if '*' in lst:
            index = lst.index('*')
            res = lst[index - 1] * lst[index + 1]
            lst[index] = res
            del (lst[index + 1])
            del (lst[index - 1])

        elif '/' in lst:
            index = lst.index('/')
            res = lst[index - 1] / lst[index + 1]
            lst[index] = res
            del (lst[index + 1])
            del (lst[index - 1])
        elif '*' and '/' not in lst:
            break
    print(lst)
    while len(lst) != 1:
        for i in lst:
            if i == '+':
                index = lst.index('+')
                res = lst[index - 1] + lst[index + 1]
                lst[index] = res
                del (lst[index + 1])
                del (lst[index - 1])
                pass
            if i == '-':
                index = lst.index('-')
                res = lst[index - 1] - lst[index + 1]
                lst[index] = res
                del (lst[index + 1])
                del (lst[index - 1])
    print(lst)
    return s + str(lst[0])


print(counter(primer()))