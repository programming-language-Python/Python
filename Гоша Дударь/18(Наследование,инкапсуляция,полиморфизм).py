'''
наследование - когда создаём ещё один класс и
этот класс унаследует все поля и все функции и
методы из основнового класса
'''
'''
class Person:
    name='Иван' # в классе переменные это поля
    age=26
    def set(self,name,age): # в классе функции это методы. self обязательна в написании
        self.name=name # self.name - это самое первое поле, а name - это параметр в функции
        self.age=age
class Student (Person): # Person- класс из которого наследуем
    course=1
Igor=Student ()
Igor.set ('Игорь', 25)
print(Igor.name)
print(Igor.course)

Vlad=Person()
Vlad.set('Влад',30)
print (Vlad.name + ' ' + str(Vlad.age))
'''
'''
Инкапсуляция( _ - для программистов показывает, 
что не стоит использовать данный метод. __ - более
строгое выдаёт ошибку) - защита данных. Ограничение доступа к
полям или методам.
'''
# _
'''
class Person:
    _name='Иван' # в классе переменные это поля
    age=26
    def _set(self,name,age): # в классе функции это методы. self обязательна в написании
        self.name=name # self.name - это самое первое поле, а name - это параметр в функции
        self.age=age
class Student (Person): # Person- класс из которого наследуем
    course=1
Igor=Student ()
Igor._set ('Игорь', 25)
print(Igor.name)
print(Igor.course)

Vlad=Person()
Vlad._set('Влад',30)
print (Vlad.name + ' ' + str(Vlad.age))
'''
# __
'''
class Person:
    name='Иван' # в классе переменные это поля
    age=26
    def __set(self,name,age): # в классе функции это методы. self обязательна в написании
        self.name=name # self.name - это самое первое поле, а name - это параметр в функции
        self.age=age
class Student (Person): # Person- класс из которого наследуем
    course=1
Igor=Student ()
Igor._Person__set ('Игорь', 25)
print(Igor.name)
print(Igor.course)

Vlad=Person()
Vlad._Person__set('Влад',30)
print (Vlad.name + ' ' + str(Vlad.age))
'''
# Полиморфизм - можем использовать один и тот же
# метод, но по-разному в разных классах
# пример:
# ипользуются разные классы (integer, string)
print(2+2)
print('2'+'2')
