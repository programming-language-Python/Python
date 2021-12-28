'''
Функция find() определяет, входит ли строка
в строке, или подстроки в строке,
от начального индекса beg и заканчивая
индексом end.
Синтаксис
str.find(str, beg = 0 end = len(string)
'''
'''
Функция rfind() возвращает последний
индекс, в котором находится подстрока
str, или -1, если такой индекс
отсутствует, дополнительно ограничивая
поиск строкой [best:end].
Синтаксис
str.rfind(str, beg = 0 end = len(string))
'''
s = input('Введите строку с двумя буквама "а": ')
a = s[:s.find('а')]  # интервал от 0 до первой "а"
b = s[s.find('а'):s.rfind('а') + 1]  # интервал от первой "а" до второй "а"
c = s[s.rfind('а') + 1:]  # интервал от второй "а" до конца
s = a + b[::-1] + c  # соединяем получившиеся интервалы и переворачиваем строку b
print(s)
