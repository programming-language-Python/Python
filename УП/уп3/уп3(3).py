import re

a = input("Введите число в двоичной системе счисления: ")

e = re.findall('(\d+)', a)  # проверяет на присутствие чисел???
if bool(e) == True and bool(a.count('2')) == False and bool(a.count('3')) == False and bool(
        a.count('4')) == False and bool(a.count('5')) == False and bool(a.count('6')) == False and bool(
    a.count('7')) == False and bool(a.count('8')) == False and bool(a.count('9')) == False:
    b = ''.join(reversed(a))
    # print(b)
    c = len(b) - 1
    n = 0
    j = 0
    while n <= c:
        for i in b:
            j += int(i) * 2 ** n
            n += 1
    print(j)
else:
    print("Вы ввели не ту систему счисления")
