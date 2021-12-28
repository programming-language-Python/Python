name = 'Swaroop' # Это объект строки
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')
if 'a' in name: 
    print('Да, она содержит строку "a"')
if name.find('war') != -1: # Метод find используется для определения позиции данной подстроки в строке; find возвращает -1, если подстрока не обнаружена
    print('Да, она содержит строку "war"')
delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))