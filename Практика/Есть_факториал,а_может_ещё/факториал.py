def fact(n):
#Возвращает факториал заданного числа.
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r
print (fact(5))