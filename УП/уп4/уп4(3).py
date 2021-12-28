# для изменения строки необходима переменная
stroka=input("Строка: ")
stroka=stroka.replace('5','пять')
stroka=stroka.replace('1','один')
print(stroka)
'''
for n in stroka:
    if n=='5':
        n="пять"
    elif n=='1':
        n="один"
    print(n, end='')
'''