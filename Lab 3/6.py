#unsiger long в С++ может содержать до 4,294,967,295
#Вы можете самостоятельно изменить размер в переменной S
s = 4294967295
n = 1
f = 1
while(f <= s):
    n += 1
    f *= n
print("Факториал можно посчитать для N равного", n-1)