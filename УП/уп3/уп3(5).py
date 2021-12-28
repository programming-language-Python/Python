a1 = input("Пол: ")
a = float(input("Вес: "))
b1 = input("Пол: ")
b = float(input("Вес: "))
c1 = input("Пол: ")
c = float(input("Вес: "))
d1 = input("Пол: ")
d = float(input("Вес: "))
x = 1.5
y = 1
year = 1
while year <= 3:
    if a1 == "м":
        a += x
    elif a1 == "ж":
        a += y
    if b1 == "м":
        b += x
    elif b1 == "ж":
        b += y
    if c1 == "м":
        c += x
    elif c1 == "ж":
        c += y
    if d1 == "м":
        d += x
    elif d1 == "ж":
        d += y
    year += 1
suma = (a + b + c + d) + (a + b + c + d) * 0.165
print("Вес экипажа на Земле " + str(suma))
