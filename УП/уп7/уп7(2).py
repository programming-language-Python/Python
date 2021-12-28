import sys
a1=input("Пол: ")
a=float(input("Вес: "))
b1=input("Пол: ")
b=float(input("Вес: "))
c1=input("Пол: ")
c=float(input("Вес: "))
d1=input("Пол: ")
d=float(input("Вес: "))
n=int(sys.stdin.readline()) # int(input("Сколько лет лететь до Земли?: "))
z=0.165
s=0
year=1
def func (вес,величина,лет):
    вес+=величина*лет
    return вес        
if a1=='м':
    s+=func(a,1.5,n)
elif a1=='ж':
    s+=func(a,1,n)
if b1=='м':
    s+=func(b,1.5,n)
elif b1=='ж':
    s+=func(b,1,n)
if c1=='м':
    s+=func(c,1.5,n)
elif c1=='ж':
    s+=func(c,1,n)
if d1=='м':
    s+=func(d,1.5,n)
elif d1=='ж':
    s+=func(d,1,n)         
suma=s+s*0.165
print("Вес экипажа на Земле " + str(suma))