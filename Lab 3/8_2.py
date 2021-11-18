n = int(input("Введите N "))
summa = 0

for x in range(10,50+1,5): #все числа были умнодена на 10, так как range не может принимать значения float
    x=x/10
    for j in (1,n+1):
        summa +=(2*n)*(x**n)
print("Ответ ",summa)