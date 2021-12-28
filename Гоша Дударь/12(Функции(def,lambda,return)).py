'''
def func(x): # передаётся 100
    def add(a): # передаётся 200
        return x+a
    return add
test=func(100)
print(test(200))

def func1(*args): # возращает не ограниченное количество параметров
    return args
print(func1(1,2,3)) # вернёт кортеж - нельзя изменить

def func1(**args): # возращает не ограниченное количество параметров
    return args
print(func1(a=5,b=56, c =90)) # вернёт словарь
'''
# lambda - анонимная функция. Выполняет только одну операцию
add=lambda x,y:x+y
print(add(2,3))
# ИЛИ
print ((lambda x,y:x*y)('ц',3))
 
fun = lambda *args: args
print(fun('Hello','World','!'))