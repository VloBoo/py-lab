from math import *
for x in range(200,500 + 1, 25): #все числа умножены на 100, так как range не принимает тип Float
    x = x / 100
    if x>3.5:
        y = sin(x) * log(x, 10)
        print("x = ",x,"\ty = ",y,"\t Вычисление идет по первой ветке")
    else:
        y = sin(x)**2
        print("x = ",x,"\ty = ",y,"\t Вычисление идет по второй ветке")