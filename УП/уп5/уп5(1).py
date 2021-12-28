from random import randint
l = list()
n = int(input("Введите количество чисел в списке: "))
m = 1
while m <= n:
    ch = randint(0, 10000)
    l.append(ch)
    m += 1
print(l)
print(sum(l))
mi = min(l)
ma = max(l)
print("Индекс минимального числа = "+str(l.index(mi)) +
      "\nИндекс максимального числа = "+str(l.index(ma)))
print("Разность между минимальным и максимальным числом = "+str(abs(mi-ma)))
