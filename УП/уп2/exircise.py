# h-час
# m- минута
# условие:
# преподаватель ведёт занятие с 10.30 до 12.00 ,
# с 13.40 до 15.00, с 18.00 до 19.30.
# В университет преподаватель приходит в 10.00,
# а уходит в 20.00. Во время свободных от пары времени- консультации.
# Напишите программу, которая поможет подстроиться под время прихода преподавателя и консультаций
# h = int(input('Введите часы: ')) * 60
# m = int(input('Введите минуты: '))
# time = h + m
# if 630 < time < 720 or 820 < time < 900 or 1080 < time < 1170:
#     print(True)
# else:
#     print(False)

# Баба Галя ходит на рынок по понедельникам, вторникам, средам.
# Четверг, пятница- ЖЭК. Суббота, Воскресенье- отдыхает на лавочке.
# В зависимости от даты узнать, когда и где она бывает. (от 1-30)
# месяц устанавливается пользователем
# end_day_months = int(input('Введи последний день месяца: '))
# day = int(input('Введи свой день: ')) % 7
# print(day)
# if 1 <= day <= 3:
#     print('Ходит на рынок')
# elif 4 <= day <= 5:
#     print('ЖЭК')
# elif 6 <= day <= 7 or day == 0:
#     print('Отдыхает на лавочке')
day = int(input('Выбраный день: '))
day_week = int(input('С какой недели начинается месяц (ввести число): '))
res = (day-day_week) % 7
if res == 0 or res <= 7:
    print ('Лавка')
elif res <= 3:
    print ('Рынок')
else:
    print('ЖЭК')
