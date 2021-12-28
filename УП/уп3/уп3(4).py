a = int(input("Высота: "))
b = int(input("Ширина: "))
x = 1
if a != 0 and b != 0:
    while x <= a: 
        print(" * " * b)
        x += 1
