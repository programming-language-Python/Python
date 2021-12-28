weight = int(input('Введите свой вес: '))
height = float(input('Введите свой рост (пример: 1.8): '))
imt = weight / height ** 2
if weight < 0 or height < 0:
    print('Ошибка. Вводить отрицательные числа нельзя')
elif 18.5 < imt < 24.99:
    res = 'Норма'
elif imt < 18.5:
    res = 'Недостаточная масса тела'
else:

    res = 'Избыточная масса тела'
print('ИМТ =', str(imt) + '\n' + str(res))
