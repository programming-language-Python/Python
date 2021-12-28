balance = float(input('Введите свою оставшуюся зарплату: '))
if balance > 5000:
    res = 'Сегодня твой выбор - ресторан!'
elif 2500 < balance < 5000:
    res = 'Эх, только фастфуд'
elif balance < 0:
    res = 'Беда!!! Иди зарабатывай'
else:
    res = 'Придётся потерпеть!'
print(res)
