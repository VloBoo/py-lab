from math import *
x = float(input("Введите знаечние x\n"))
if x == 0 or x == -1:
    print("Х не может быть равен 0 или -1")
else:
    y = ( cos(exp(x)) + log(1+x) + (exp(cos(x))+ sin(x)**2 * x * pi)**0.5 + (1/x)**0.5 + cos(x**2))**sin(x)
    print(y)