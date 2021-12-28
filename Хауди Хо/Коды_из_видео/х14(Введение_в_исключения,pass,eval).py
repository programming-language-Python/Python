'''
print("Test")q # Выведит SyntaxError: invalid syntax это является исключением
print (8/0) # это тоже исключение ZeroDivisionError: division by zero
При исключении(возникновении ошибки) код программы останавливается
'''
# Процесс исключения обработки
''' 
Исключения бывают(Основыне 6 исключания):
ImportError, IndexError(при не существовании индекса в списке),
NameError(нет такой переменной), SyntaxError, TypeError, 
ValueError(возникает, когда тип переданной переменной или значения тот, что нужен, 
но занчение не такое, что нужно)
'''
'''
try: # берём поведение под контроль
    print(7/0)
except ZeroDivisionError: # пишем какое хотим поймать исключение
    print("Поймано исключение ZeroDivisionError")
print('Программа завершена!')
try: # берём поведение под контроль
    print(7/0)
except ZeroDivisionError: # пишем какое хотим поймать исключение. Если не писать никакое исключение(ошибку), то будут пойманы все исключения(ошибки)
    pass # Ключевое слово pass. Это значит пропустить, т.е. ничего не выводит. Если ничего не писать то появиться ошибка IndentationError
print('Программа завершена!')
# в Python всё идёт слева на право и сверху вниз. По этому ниже выведится только ZeroDivisionError, т.к. это ошибка идёт первее
try: # берём поведение под контроль
    print(7/0)
    d
except ZeroDivisionError: # пишем какое хотим поймать исключение. Если не писать никакое исключение(ошибку), то будут пойманы все исключения(ошибки)
    print("Поймано исключение ZeroDivisionError")
except NameError: # пишем какое хотим поймать исключение. Если не писать никакое исключение(ошибку), то будут пойманы все исключения(ошибки)
    print("Поймано исключение NameError")
print('Программа завершена!')
# Не ловит SyntaxError. Чтоб её поймать понадобится eval()
try: # берём поведение под контроль
    eval('print(7/0)a')
except ZeroDivisionError:
    print("Поймано исключение ZeroDivisionError")
except SyntaxError:
    print("Поймано исключение SyntaxError")
print('Программа завершена!')
try:
    print(7/2)
except (ZeroDivisionError, NameError):
    print("Поймано исключение ZeroDivisionError или NameError")
print('Программа завершена!')

try:
    print(7/2)
except (ZeroDivisionError, NameError):
    print("Поймано исключение ZeroDivisionError или NameError")
finally: # Исполняет код вне зависимости было ли поймано исключение или нет
    print("Конец поимки")
print('Программа завершена!')

# можно свои создавать исключения. При скачивании модулей могут быть в них свои исключения
try:
    pogoda="Плохая"
    if pogoda=="Плохая":
        raise TypeError
except TypeError:
    print("Поймано исключение TypeError")

try: 
    pogoda="Плохая"
    if pogoda=="Плохая":
        raise TypeError('Тест') # выбрасивает причину ошибки
except:
    print("Пойман!!!")

try: 
    print(7/0)
except:
    print("Тест")
    raise # выбрасивыет исключение по которому был вызван
'''
# Создания своего типа исключения
class Rom(Exception):
    pass # обычно пишется условия, его поведения и т.д.
raise Rom("test")