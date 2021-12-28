'''Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?'''
import math
def issimple(n):
    r=math.ceil(math.sqrt(n))
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=5
s=[2,3]
while True:
    if issimple(n) is True:
        s.append(n)
    if len(s)==10001:
        break
    n+=2
print(s[-1])

'''n=1
k=2
p=0
for n in range(k):
    for a in range (1, n):
        if (n % a) == 0:
            k+=1
            break
        elif (n // a) == 1:
            print ("Число ", n, " простое!")
            p+=1
            k+=1
            break
    if p==3:
        break'''    
'''
import fractions
k=10001
arr=[i for i in range(k) if i!=0 and i%i==0]
print (arr)
'''
'''
k=10
a=[]
for i in range(k):
    for j in range(2,10):
        if i%j!=0 and i//i==1:
            a.append(i)
        else:
            k+=1
print (a)

b=[]
for i in range (15):
    if i!=0 and i!=1:
        for j in range (2,10):
            if i!=j:
                if fractions.gcd(i,j)==i:
                    b.append(i)
print(b)
'''