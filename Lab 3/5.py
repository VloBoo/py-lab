n = int(input("Введите число N"))
m = int(input("Введите число M"))

while n > 0:
    p = n - 1
    while p > 1:
        if n % p == 0:
            break
        p -=1
    else:
        p = n
        s = 0
        while p != 0:
            s += p % 10
            p = p // 10
        if s < m :
            print(n)
    n -=1