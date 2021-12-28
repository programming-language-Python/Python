'''
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 52.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
'''
while True:
    for a in range(100, 1000):
        for b in range(100, 1000):
            c=pow(a**2+b**2,0.5)
            if a==b:
                continue
            elif a<b<c and c**2==a**2+b**2 and a+b+c==1000:
                break
        if a<b<c and c**2==a**2+b**2 and a+b+c==1000:
            break
    if a<b<c and c**2==a**2+b**2 and a+b+c==1000:
        break
print(a)
print(b)
print(c)