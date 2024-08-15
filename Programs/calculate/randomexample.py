import random as rnd


def primer():
    was = False
    znaki = ('+', '-', '*', '/')
    znakidel = ('+', '-', '*')
    lst = []
    for i in range(rnd.randint(3, 5)):
        rndznak = rnd.choice(znaki)
        if was is False and rndznak == '/':
            lst.append(rnd.randint(1, 20))
            lst.append(rndznak)
            was = True
        elif was is False and rndznak != '/':
            lst.append(rnd.randint(1, 20))
            lst.append(rndznak)
        elif was is True and rndznak == '/':
            rndznak = rnd.choice(znakidel)
            lst.append(rnd.randint(1, 20))
            lst.append(rndznak)
        elif was is True and rndznak != '/':
            lst.append(rnd.randint(1, 20))
            lst.append(rndznak)
    lst.pop()
    return lst


def counter(lst):
    s = ''
    for i in lst:
        s += str(i)
    s += '='
    print(lst)


    while len(lst) != 1:
        for i in lst:
            print(lst)
            if i == '*':
                index = lst.index('*')
                res = lst[index - 1] * lst[index + 1]
                lst[index] = res
                del (lst[index + 1])
                del (lst[index - 1])

            if i == '/':
                index = lst.index('/')
                res = lst[index - 1] / lst[index + 1]
                lst[index] = res
                del (lst[index + 1])
                del (lst[index - 1])
            if '/' and '*' not in lst:
                pass
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
