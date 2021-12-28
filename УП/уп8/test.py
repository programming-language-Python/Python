# r - открыть на чтение
# w - открыть на запись (код удаляется)
# x - октрытие на запись если файла не существует
# a - открытие на дозапись
# b - открыть в бинарном режиме
# t - открытие в текстовом режиме
# + - открытие на чтение и на запись
# f = open('D:/Users/maks2/Desktop/Программирование/PYTHON/УП/уп8/text.txt', 'r')
# f.read(1)  # аргумент это номер символа
# for line in f:
#     print(line)
# f.close()
# l = [str(i) + str(i-1) for i in range(20)]
# d = open('D:/Users/maks2/Desktop/Программирование/PYTHON/УП/уп8/text2.txt', 'w')
# for index in l:
#     d.write(index + '\n')
# d.write('end')
# d.close()
# r = open('D:/Users/maks2/Desktop/Программирование/PYTHON/УП/уп8/text2.txt', 'r')
# r.read(1)
# for li in r:
#     print(li)
# r.close()

import os
print(os.getcwd())  # выводит домашний каталог
os.chdir('AppData/Roaming')  # переход в выбранный каталог
print(os.getcwd())
# os.listdir(os.curdir())
