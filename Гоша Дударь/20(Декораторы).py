# Декораторы - обёртка для функций. Функцию
# завернуть в другую функцию. Замедляют вызов 
# функции. Рекомендуется не зло употреблять.
'''
def decorate(func):
    def wrapper():
        print("Код до выполнения функции")
        func()
        print("Код, который сработал после функции")
    return wrapper
@decorate # создали декоратор
def show():
    print("Я обычная функция")
# dec = decorate(show) # создали декоратор
# dec()
show()
'''
def decorate(func):
    def wrapper():
        print("Код до выполнения функции")
        func()
        print("Код, который сработал после функции")
    return wrapper
def qwe(func):
    def wrapper():
        print("Код до выполнения функции 2")
        func()
        print("Код, который сработал после функции 2")
    return wrapper
@decorate # создали декоратор
@qwe
def show():
    print("Я обычная функция")
# dec = decorate(show) # создали декоратор
# dec()
show()