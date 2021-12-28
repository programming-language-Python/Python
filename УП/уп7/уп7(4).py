import datetime
d = datetime.datetime.today()
мин = d.minute
if мин == 30:
    print('Дата:', d.strftime("%d"), '\nВремя:',
          d.strftime("%H:%M:%S"), '\nХочу есть')
elif мин % 2 == 0:
    print('Минута в настоящее время является четной')
elif мин % 2 != 0:
    print('Минута в настоящее время является нечетной')
