from math import *
print("Расположение фигур от 1 до 8:\n")
konX = int(input("Введите расположение коня по x\n"))
konY = int(input("Введите расположение коня по y\n"))
slonX = int(input("Введите расположение слона по x\n"))
slonY = int(input("Введите расположение слона по y\n"))

if konX < 1 or konX > 8 or konY < 1 or konY > 8: #проверяем расположение коня
    print("Ошибка ввода расположения коня")
elif slonX < 1 or slonX > 8 or slonY < 1 or slonY > 8: #проверяем расположение слона
    print("Ошибка ввода расположения слона")
else:

    if (konX+2 == slonX or konX-2 == slonX) and (konY+1 == slonY or konY-1 == slonY) or (konX+1 == slonX or konX-1 == slonX) and (konY+2 == slonY or konY-2 == slonY): #проверяем ходы коня
        print("Конь угрожает слону")
    elif abs(konX-slonX) == abs(konY-slonY): #проверяем ход слона
        print("Слон угрожает коню")
    else:   
        print("Фигуры в безопастности")
       