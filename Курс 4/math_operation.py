# res = (((10 + 14 ** 5) ** 2 * 7 ** 7) / (6 ** 3 + (3 ** 3) ** 3 + 91 ** 3)) ** 1 / 2
# print(res)
#
# # найти сумму 1 + 2 + ... + n. n вводит пользователь контрольное число 100
# num = int(input('Введи 100 (ответ должен быть 5050): '))
# sum = 0
# for i in range(1, num + 1):
#     sum += i
# print(sum)

# найти все 4-х значные числа сумма цифр которых равна 30
for num in range(1000, 10000):
    list_number = list(int(number) for number in str(num))
    if sum(list_number) == 30:
        print("Сумма цифр числа", num, "равна 30")
