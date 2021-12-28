'''
a1=input("Пол: ")
a=float(input("Вес: "))
b1=input("Пол: ")
b=float(input("Вес: "))
c1=input("Пол: ")
c=float(input("Вес: "))
d1=input("Пол: ")
d=float(input("Вес: "))
z=0.165
year=1
def func (пол, вес, величина=4.5):
    if пол=="м":
        вес+=величина
        return вес        
    elif пол=="ж":
        величина=3
        вес+=величина
        return вес    
b=func(a1,a) + func(b1,b) + func (c1,c) + func(d1,d)
suma=b+(b)*0.165
print("Вес экипажа на Земле " + str(suma))
'''
# по заданию
a1=input("Пол: ")
a=float(input("Вес: "))
b1=input("Пол: ")
b=float(input("Вес: "))
c1=input("Пол: ")
c=float(input("Вес: "))
d1=input("Пол: ")
d=float(input("Вес: "))
s=0
z=0.165
year=1
def func (вес, величина):
    вес+=величина
    return вес
if a1=='м':
    s+=func(a,4.5)
elif a1=='ж':
    s+=func(a,3)
if b1=='м':
    s+=func(b,4.5)
elif b1=='ж':
    s+=func(b,3)
if c1=='м':
    s+=func(c,4.5)
elif c1=='ж':
    s+=func(c,3)
if d1=='м':
    s+=func(d,4.5)
elif d1=='ж':
    s+=func(d,3)    
suma=s+(s)*0.165
print("Вес экипажа на Земле " + str(suma))

