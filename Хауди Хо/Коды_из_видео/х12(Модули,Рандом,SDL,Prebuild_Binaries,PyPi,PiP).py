'''
# модуль - это python файл. Определённые функции, группы
# надо подключить модуль
import random
# появляется объект random
print(random.randint(1,100)) # randint() - это функция
for i in range(10):
    print(random.randint(1,100))
import math
num=10
print(math.sqrt(num))
# получение отдельных функций
from random import randint # получили функцию raindint()
print(randint(1,100))
from random import * # из модуля random импортировать всё
from math import *
print(pi)
print(sqrt(25))
from math import sqrt, pi # импорт нескольких функций
from math import sqrt as my_sqrt # переменновали в my_sqrt
def sqrt(): # делается для того, чтобы не возникли колфликты между функциями
    print('my function')
    print(my_sqrt(25))
sqrt()
'''
'''
Модули делятся на 3 типа, которые сами написали, 
загрузили с интернета(внешнии модули), 
которые сами установленны в python(STL/SDL???).
Интегрированные модули(STL/SDL???): random, math, 
r - для регулярных выражений, datetime,
 os для получение информации ОС,
email, json(джейсон) для работы 
с кодированными данными, 
sys для получ. данных о системе
PyPi - сайт с модулями.
Есть: распознавание голоса, соединение с youtube
В командей строке пишем pip и выведится информация о нём
Для установки модуля надо написать pip install "название модуля из интернета"
И для его использования пишем в коде import "название модуля"
'''