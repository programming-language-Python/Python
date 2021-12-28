x = int(input("Введите прошедшие минуты: "))
res = x % 5
if x < 0:
    print('Ошибка! Вы ввели отрицательное число')
elif res == 0 or res == 4:
    print("Красный")
elif 1 <= res <= 3:
    print("Зелённый")