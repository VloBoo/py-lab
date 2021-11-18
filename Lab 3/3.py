m = int(input("Введите число M"))
n = int(input("Введите число N"))
s = 0
while m>1:
    i = 2
    while i <= m:
        if m % i == 0 and n % i ==0:
            s += 1
        i += 1
    m -= 1
print("Было найдено взаимно простых чисел:", s)