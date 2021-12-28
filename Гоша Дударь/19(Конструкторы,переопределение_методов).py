# Конструктор (__init__)
'''
class Person:
    name='Иван' 
    age=26
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __set(self,name,age):
        self.name=name
        self.age=age
class Student (Person):
    course=1
Igor=Student ('Игорь',25)
# Igor._Person__set ('Игорь', 25)
print(Igor.name)
print(Igor.course)

Vlad=Person('Влад',56)
# Vlad._Person__set('Влад',30)
print (Vlad.name + ' ' + str(Vlad.age))

vaca=Student ('Вася',20)
print(vaca.name)
'''
# Переопределение методов
class Person:
    name='Иван' 
    age=26
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def set(self,name,age):
        self.name=name
        self.age=age
class Student (Person):
    course=1
    def set(self,name,age,course): # переопределение метода
        self.name=name 
        self.age=age
        self.course=course
Igor=Student ('Игорь',25)
# Igor._Person__set ('Игорь', 25)
Igor.set ('Игорь', 25, 4)
print(Igor.name)
print(Igor.age)
print(Igor.course)

Vlad=Person('Влад',56)
# Vlad._Person__set('Влад',30)
print (Vlad.name + ' ' + str(Vlad.age))

vaca=Student ('Вася',20)
print(vaca.name)