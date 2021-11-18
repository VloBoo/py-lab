n = int(input("Введите N :"))
summa = 1
summaS = 0 
summaC = 0

for i in range(1, n+1):
    print("Введите C",i,":")
    summaC += int(input())
    print("Введите S",i,":")
    summaS += int(input())
    summa *= (summaC/summaS)
print("Ответ ",summa)    