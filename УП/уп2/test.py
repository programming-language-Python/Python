# name = input("Введи имя: ")
# text_1 = ("Привет, меня зовут {0}.{1} хочет кушать.{1} хочет спать.{0} не хочет учится". format(
#     name, 'Саша'))
# len_text = len(text_1)
# bool_text = bool(len_text)
# bool_false = (str('a'+'5')+'7')
# print("первая-{0},\nвторая-{1}". format(bool_text,bool_false))
# print("первая",bool_text,"\n вторая-",bool_false)


# if, else
# a=int(input("введи а: "))
# if a <= 5:
#     if a<2:
#         print("a от минус бесконечности до 1")
#     else:
#         print("это 2,3,4.5")
# else:
#     print("a больше 5")

word = "Ехал Грека через реку,\nвидит Грека в реке рак"
if 'р' in word:
    print("Вау! Тут буква 'р'!")
elif 'з' in word:
    print("неужели! тут 'з'")
else:
    print('ХАХА')
