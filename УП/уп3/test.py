# a = 2
# b = 5
# c = 1
# for i in range(a, b, c):
#     i += 1
#     print(i ** i)

# на четность диапозон от 30 до 41
# for i in range(30, 41):
#     if i % 2 == 0:
#         print('Это чило чётное')
#     else:
#         print('Это число нечётное')

# вывести пару счётчик элемент для строки вводимой пользователем
# enumerate()
# word = str(input('Введи текст: '))
# for i, letter in enumerate(word):
#     print(i,letter)

# написать программу которая принимает на вход запись пользователя и выводит из неё только гласные буквы
arr_a = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
user = str(input('Введи слово: '))
for i, letter in enumerate(user):
    for a in arr_a:
        if letter == a:
            print(a)
