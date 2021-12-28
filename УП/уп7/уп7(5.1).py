import calendar
while True:
    my = input('Введите через пробел месяц(числом) и год: ')
    my = my.split(' ')
    if len(my) > 2 or len(my) < 2:
        print('Ошибка! Введите один месяц и один год через пробел')
    elif int(my[0]) < 0 or int(my[1]) < 0:
        print('Ошибка! Нельзя вводить отрицательное числа')
    else:
        break
calendar.prmonth(int(my[1]), int(my[0]))
