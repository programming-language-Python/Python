i=0
while i<10:
    print(i)
    i+=2
for j in 'Hello world':
    print(j*2,end='') # end='' выводит всё на одной строчке
# операторы
for j in 'Hello world':
    if j =='w':
        continue # пропускает одну операцию
    print(j*2,end='') # end='' выводит всё на одной строчке
for j in 'Hello world':
    if j =='w':
        break # выходит из цикла
    print(j*2,end='') # end='' выводит всё на одной строчке

for j in 'Hello world':
    if j =='a':
        break
    print(j*2,end='') # end='' выводит всё на одной строчке
else: # если не разу не сработал break, то сработает else
    print(" Буквы а нету в слове")