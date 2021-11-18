from math import *

x = 2.0 
while x <= 5:
    y=0
    if x>3.5:
        y = sin(x) * log(x, 10)
        print("x = ",x,"\ty = ",y,"\t Вычисление идет по первой ветке")
    else:
        y = sin(x)**2
        print("x = ",x,"\ty = ",y,"\t Вычисление идет по второй ветке")
    x = x + 0.25