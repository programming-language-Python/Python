digits=[1,2,3,4,5,6,7,8,9,10]
'''
digits2=digits[2:5] # срез списка 2<5
print(digits2)

# пропуск индекса среза
digits2=digits[:3] # c начало до 2
print(digits2)
digits2=digits[3:] # с 3 до конца
print(digits2)

# шаги списка
digits2=digits[::2]
print(digits2)
digits2=range(1,101)[::2] # генерирует чётные числа
for i in digits2:
    print(i)
'''
digits2=digits[-2]
print(digits2)

digits2=digits[-4:-1] # выводит слева на право
print(digits2)

digits2=digits[::-1] # реверсирование
print(digits2)

digits2=digits[::-1][::1]
print(digits2)