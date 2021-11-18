n = int(input("Введите N "))
#x = float(input("Введите X ")) в данном варианте x не требуеться
summa = 0

for i in range(1, n+1):
    proizved = 1
    for j in (1, i+1):
        proizved *= (i - j)/(i + j)
    summa += proizved
print("Ответ ",summa)