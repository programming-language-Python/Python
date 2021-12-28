# Вариант 1
словарь = {'год': ['время'], 'дело': ['работа'], 'солнце': ['свет'], 'круг': [
    'окружность'], 'квадрат': ['прямоугольник'], 'трава': ['зелень']}
end = sorted(словарь.keys())[-1]
син = input('Для слова ' + '\'' + end + '\'' +
            ' из словаря записанного в последней строке, определите синоним: ')
if син in словарь[end]:
    print('Да есть такой синоним для слова ' + end)
else:
    выбор = input('Синоним ' + син + ' для слова ' + end +
                  ' нет. Желаете ли добавить этот синоним к данному слову? (да/нет) ')
    if выбор == 'да':
        словарь[end].append(син)
        print('Слово добавленно')

# Вариант 2
# слово=input('Введите слово для проверки синонима: ')
# if слово in словарь:
#     print('Данное слово существует\nЕё синонимы ' + str(словарь[слово]))
# elif not слово in словарь:
#     for i in словарь:
#         if слово in словарь.get(i):
#             print('Введённое слово в словаре является синонимом')
# else:
#     print('Данного слова не существует')
#     выбор1=input('Желаете добавить это слово и синоним для него? (да/нет) ')
#     if выбор1=='да':
#         син1=input('Введите синоним для слова ' + слово + ' ')
#         словарь.update({слово:[син1]})
#         print(словарь)
