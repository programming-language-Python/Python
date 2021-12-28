# (join, replace,startswith, endswith, lower, upper, split,) - методы строки (min, max, abs, sum) - функции чисел

fruits=['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']
members='James,Jonny,Jessie,Jack,Jonh'
'''
# join - превращает из списка в строку
print(','.join(fruits)) # превращает из списка в строку. Первый символ показывает чем будут разделяться значения
# replace - заменяет значения
print('Привет, Пётр!'.replace('Пётр', 'Александр')) # Заменяет значения. Регистро зависимый
# startswith - с чего начинается
name=input('Ваше имя: ')
if name.startswith('А'): # с чего начинается
    print('Вы из элитных группы людей!')
else:
    print('Добро пожаловать!')
# lower - переводит всю строку в нижний регистр
if name.lower().startswith('а') or name.lower().startswith('a'): # с чего начинается. Русская буква 'а' англ буква 'a'
    print('Вы из элитных группы людей!')
else:
    print('Добро пожаловать!')

input_str=input('Введи: ')
print(input_str.lower())
# endswith - с чего заканчивается
word='Hello dridving'
if word.endswith('ing'):
    print('Hello ING!')
else:
    print('No ING!!!')
# upper - перевод в верхний регистр
input_str=input('Введи хоть что: ')
print(input_str.upper())
'''
# split - произвести обратное действие join. Строку разбивает в список или в кортеж
print (members.split(',')) # первым аргументом указываем признак соединителя (чем соединяются слова)
# min
print(min ([5,12,34,543,43,1]))
# max
print(max ([5,12,34,543,43,1]))
# abs
print(abs(-1203))
# sum
print(sum([11,3,4,12]))