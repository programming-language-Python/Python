'''Строка документации'''
def h():# функция это переменная 
    '''Строка документации'''
    print('Hell')
print(h.__doc__) # __doc__ выводит строку документации(комментарий в функции)
my=h
my()
'''
def red(color):
    print('Color: ' + color + '!')
red("green")

def read():
    return input('Введите цвет ')
red(read())
'''
def red(color):
    print('Color: ' + color() + '!')
def read():
    return input('Введите цвет ')
red(read) # передаёт функцию в аргумент 