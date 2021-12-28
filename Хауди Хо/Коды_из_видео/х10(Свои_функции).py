# print(), str(), float(), list() это функции
def print_span(): # создание своей функции
    print('span')
    print('span')
    print('span')
print_span()
print_span()
# аргументы функции
def mul(number): # number - параметр
    print(number * 2)
mul(2) # 2 - аргумент
def max(x, y):
    if x>y:
        return x # выводит x и завершает саму функцию
    else: 
        return y
x=int(input("Число1: "))
y=int(input("Число2: "))
print(max(x,y))