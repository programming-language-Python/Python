a = [int(s) for s in input('Введите числа в список через пробел: ').split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

'''
# НЕ ПРАВИЛЬНО (берёт находит пару и уберает эту пару ищит следующую)
# через множество
ввод=input('Введите числа в список через пробел: ')
lis=ввод.split(' ') # преобразование из строки в список
print(lis)
s=set(lis) # преобразование в множество
print(s)
summa=0
for i in s:
    # считаем количество элементов
    if lis.count(i)%2==0: # если чётное количество пар
        summa+=lis.count(i)
    if lis.count(i)%2==1: # если нечётное количество пар
        summa+=(lis.count(i)-1)
print (int(summa/2))

# по заданию
ввод=input('Введите числа в список через пробел: ')
lis=ввод.split(' ') # преобразование из строки в список
print(lis)
lisno=[]
summa=0
# создаём новый список в котором будут все элементы, которые входят в список lis (без повторенний)
for i in lis:
    if i not in lisno:
        lisno.append(i)
print(lisno)
for i in lisno:
    # считаем количество элементов
    if lis.count(i)%2==0: # если чётное количество пар
        summa+=lis.count(i)
    if lis.count(i)%2==1: # если нечётное количество пар
        summa+=(lis.count(i)-1)
print (int(summa/2))
'''
