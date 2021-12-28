number = int(input('Введи число Вова: '))
if number % 2 == 0 or number % 5 == 0 or number % 173 == 0 or number % 821 == 0:
    res = 'Вова, это нужное число'
else:
    res = 'Вова, это не то число'
print(res)
