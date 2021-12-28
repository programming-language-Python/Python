# список
# c=input()
# b=input()
# a='это текст с переменными {1} и примерами {0}'.format(c,b)
# print (a)

# c=5
# b=25
# a='это текст с переменными {1} и примерами {0}'.format(c,b)
# z='это промышленный текст a:%s'
# print(z % a)

# List_1 = ['ЛАВРОВЫЙ ЛИСТ', 'СЛЕЗА ЛЯГУШКИ',
#           'НОГОТЬ ЧЕРЕПАХИ', 'УШКИ ЛЕТУЧЕЙ МЫШИ', 'ГЛАЗ ЯЩЕРИЦЫ']
# List_1.append('Перо Клювокрыла')
# del List_1[2]
# List_1[4] = 'Лапка гидры'
# List_1.insert(0, 'СЕЛЬДЕРЕЙ')
# List_1.index('УШКИ ЛЕТУЧЕЙ МЫШИ')
# print (List_1.count ('ГЛАЗ ЯЩЕРИЦЫ'))
# print (List_1[0],List_1[1::4],List_1[::2])
# print(List_1.index('УШКИ ЛЕТУЧЕЙ МЫШИ'))


# List_2 = ['Gerd', 250, 'witcher']
# List_3 = List_1 + List_2 * 10
# igra = ['спорт', 'Rpg', 'стратегия', 'гонки', 'шутер']
# igra[2] = ['nfs', 'dirt', 'firza', 'казуальные']
# igra[2] [1] = ['открытые', 'закрытые']
# print(igra)

# кортеж
# kor = (307, 308)
# print(kor,'\n',kor[0],'\n',kor[1])

# kor_text = tuple('Абакадабра')
# print(kor_text)

# словарь
# vocabulary = {
#     'Понедельник': 'День тяжёлый',
#     'Вторник': 'Сложно до сих пор',
#     'Среда': 'Нам уже полегче',
#     'Четверг': 'Поскорее бы выходной',
#     'Пятиница': 'Ещё чуть-чуть!',
#     'Суббота': 'Хочу в колледж',
#     'Воскресение': 'Осознание'
# }
# # print(vocabulary['Среда'])
# # vocabulary['Несуществующий'] = 'День'
# # print(vocabulary)
# z = 'Мои дни недели: %s'
# print(z % vocabulary.items())
# x = vocabulary.items()
# print(x)
# for item in x:
#     print(item[0],item[1])

smail = [c*5 for c in 'Кровать' if c != 'К']
print(smail)
