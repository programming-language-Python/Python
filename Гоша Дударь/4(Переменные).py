# переменные не могут начинаться с цифр (12num, $gds). Чувствительны к регистру
"""test=12
print(test)

num_1=input("Введите переменную 1: ")
num_2=input("Введите переменную 2: ")
res=num_1+num_2
print("Result: ", res)

num_1=int(input("Введите переменную 1: "))
num_2=int(input("Введите переменную 2: "))
res=int(num_1+num_2)
print("Result: ", res)
"""
# переменные с input 
"""
num_1=input("Введите переменную 1: ")
num_2=input("Введите переменную 2: ")
res=int(num_1+num_2)
print("Result: ", res)
"""
"""
num_1=input("Введите переменную 1: ")
num_2=input("Введите переменную 2: ")
res=int(num_1+num_2)
del res # удаление переменной 
print("Result: ", res)

num_1=str(21) 
print(num_1)

num_1=float(input("Введите переменную 1: "))
num_2=float(input("Введите переменную 2: "))
res=float(num_1+num_2)
res+=5 # или res=res+5 
print("Result: ", res)
"""
num_1=input("Введите переменную 1: ")
num_1*=5
print("Result: ", num_1)