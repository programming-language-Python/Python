'''
class Person:
    name='Иван'
    age=26
Vlad=Person() # Vlad - это объект класса Person()
Vlad.name='Влад'
print (Vlad.name)

Ivan=Person()
print (Ivan.name)

Ivan=Person()
Ivan.age=45
print (Ivan.age)
'''


class Person:
    name = 'Иван'  # в классе переменные это поля
    age = 26

    def set(self, name, age):  # в классе функции это методы. self обязательна в написании
        self.name = name  # self.name - это самое первое поле, а name - это параметр в функции
        self.age = age


Vlad = Person()
Vlad.set('Влад', 30)
print(Vlad.name + ' ' + str(Vlad.age))
