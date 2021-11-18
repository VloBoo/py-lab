n = int(input("Введите число N"))
while n>11:
    c = n
    s = c % 10 #s это остаток
    c = c // 10 #c целая часть
    while c != 0:
        if s - 1 != c % 10:
            break
        s = c % 10
        c = c // 10
    else:
        print(n)
    n -=1