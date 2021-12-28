#pip install pyinstaller установка модуля для отправки другу.
# команда pyinstaller -F [название файла].
# После этого появится папка dist и в этой папке находится файл exe который можно отправлять.
from colorama import init
from colorama import Fore, Back, Style #модуль 
# use Colorama to make Termcolor work on Windows too
init()
print(Fore.BLACK)
print(Back.WHITE)
# Первый калькулятор на Python
what=input("что делаем? (+,-,*,/):")
print(Back.BLUE)
a=float(input("Введи первое число:"))
b=float(input("Введи второе число:"))
 #условие 
print(Back.RED)
if what == "+": #потом ставится на следующей строчке 4 пробела
    c = a + b
    print ("Результат: " + str(c))
elif what == "-":
    c= a - b
    print ("Результат: " + str(c))
elif what == "*":
    c= a*b
    print ("Результат: " + str(c))
elif what == "/":
    c= a/b
    print ("Результат: " + str(c))
else:
    print ("Выбрана неверная операция!")

input()#для друга при отправке ему программы. Чтобы программа не закрывалась при её выполнении