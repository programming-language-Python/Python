import os
import random as r
print (os.uname()) # вся характеристика пк
print (r.random()) # рандомное число от 0 до 1

# импорт своего модуля. Создаем файл и импортируем
# нельзя называть модуль с цифрами или с резервироваными именами
'''
import modul as m
m.hi()
print (m.add(45,15))
'''
#  ИЛИ

from modul import hi as h, add as a
h()
print (a(45,15))
