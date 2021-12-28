# вариант 1
'''
from random import randint
l=list()
r=1
while r<=10:
    q=randint(-1000,1000)
    if q not in l:
        l.append(q)
        r+=1
    elif q in l:
        r-=1
print(l)
gust=int(input("Добавьте в список число: "))
ma=max(l)
mi=min(l)
ima=l.index(ma)
imi=l.index(mi)
l.remove(ma)
l.remove(mi)
l.insert(ima,mi)
l.insert(imi,ma)
if gust in l:
    print("Ошибка это число есть в списке")
else:
   l.append(gust)
print (l)
'''
# вариант 2 (по заданию)
l = list()
r = 1
while r <= 10:
    q = int(input("Добавьте в список число: "))
    if q not in l:
        l.append(q)
        r += 1
    elif q in l:
        print('ERROR число ' + str(q) + ' есть в списке.')
        r -= 1
print(l)
ma = max(l)
mi = min(l)
ima = l.index(ma)
imi = l.index(mi)
l.remove(ma)
l.remove(mi)
l.insert(ima, mi)
l.insert(imi, ma)
print(l)
