'''
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.'''
import math
def issimple(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return n
n=2000000
s=2
arr=[issimple(i) for i in range(int(n/2)+1,n,2)]
print(arr)
'''
arr=[issimple(i) for i in range(3,n,2)]
print(arr)
'''
'''
for i in range(3,int(n/100000),2):
    s+=issimple(i)
for i in range(int(n/100000+1),int(n/10000),2):
    s+=issimple(i)
for i in range(int(n/10000+1),int(n/1000),2):
    s+=issimple(i)
for i in range(int(n/1000+1),int(n/100),2):
    s+=issimple(i)
for i in range(int(n/100+1),int(n/10),2):
    s+=issimple(i)
for i in range(int(n/10+1),n,2):
    s+=issimple(i)
'''
print(s)