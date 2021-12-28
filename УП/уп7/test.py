
# import turtle
# import random
# t = turtle.Pen()
# t.forward(150)
# t.left(0)
# t.forward(56)
# t.right(50)
# t.forward(8)
# t.up()
# t.left(120)
# t.forward(60)
# t.down()
# t.color(0, 1, 1)
# t.forward(120)
# t.begin_fill()
# t.circle(60)
# t.color('black')
# t.end_fill()
# t.up()
# t.left(-20)
# t.forward(60)
# t.down()
# t.begin_fill()
# for i in range(0,12):
#     t.forward(100)
#     t.left(150)
# t.color(1,0,1)
# t.end_fill()

# t = turtle.Pen()
# t.up()
# t.left(-60)
# t.forward(70)
# t.down()
# t.begin_fill()
# for i in range(0,5):
#     t.forward(100)
#     t.left(150)
# t.color('red')
# t.end_fill()
# t.speed(-1)

# t = turtle.Pen()
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'mediumorchid',
#           'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'limegreen', 'darkgreen', 'darkorange']
# le = 100
# for i in range(100):
#     t.forward(le)
#     t.right(90)
#     le -= 1
#     t.color(random.choice(colors))

# t.end_fill()

# t.screen.mainloop()

# Функции
# синтаксис
# def название(аргумент):
#     тело
# def abb(x, y):
#     return x + y


# a = abb('abc', 'afj')
# b = abb(1, 20)
# print(str(a) + '\n' + str(b))

# def newfunc(n):
#     def myfunc(x):
#         return x + n
#     return myfunc


# print(newfunc(200)(500))
# print(newfunc(200))
# a = newfunc(200)
# print(a(500))

# В некоторых языках функция, не возращающая значение называется процедурой.
# Хотя когда в python прописываются функции в которой не прописано return такие функции не являются процедурой, но все процедуры являются функции.
# Если в теле процедуры не выполняется команда return возращается специальное значение None. При выводе return с аргументов выводится аргумент.
# После того как мы выполнили return дальше никакие действия не выполняются.
# Параметром функции можно задавать значения по умолчанию, но при этом эти значения можно изменять внутри функции.
# def jjj(a, b, c=25):
#     d = a + b / c
#     return d


# print(jjj(5, 100))
# print(jjj(10, 40, 2))

# по мимо этого можно задавать аргументы оталкиваясь от их названия.
# def jjj(b=3, c=4, a=1003):
#     print(a)
#     print(b)
#     print(c)


# jjj()
# такой способ назывется передачей по ключивым словам

# функция может содержать переменное количество аргументов
# если в имени аргумента предшествует символ * то такой аргумент будет принимать неопределённое количество значений
# def maxmin(*numbers):
#     if len(numbers) == 0:
#         return None
#     else:
#         maxnum = numbers[0]
#         for n in numbers[1:]:
#             if n > maxnum:
#                 maxnum = n
#         return maxnum

# print(maxmin(1, 2, 45, -15, 78))

# Существует такое понятие как не определённое количество аргументов предаваемых по ключевым словам.
# Если последний параметр в списке снабжён префиксом **, то все лишние аргументы передаваемые по ключевым словам объединяются в словарь.
# Ключём для каждого словаря будет ключевое слово имя этого параметра.
# def example_fun(x, y, **other):
#     print('x: {}, y: {}, keys in other: {}'.format(
#         x, y, list(other.keys())))
#     other_total = 0
#     for k in other.keys():
#         other_total += other[k]
#     print('The total of values in other is {}'.format(other_total))


# example_fun(2, y='1', foo=3, bar=4)

# все аргументы в функциях могут передаваться в виде ссылки на объект, тогда мы можем получить изменяемые объекты в качестве аргумента.
# def f(n, list1, list2):
#     list1.append(3)
#     list2 = [4, 5, 6]
#     n += 1


# x = 5
# y = [1, 2]
# z = [4, 5]
# f(x, y, z)
# print(x, y, z)

# Локальные, не локальные и глобальные переменные
# def fact(n):
#     r = 1
#     while n > 0:
#         r *= n  # локальная переменная
#         n -= 1
#     return r


# print(fact(4))

# любая переменная находящиеся только внутри функции является локальной и не выходящей за границы этой функции.
# По мимо этого переменная внутри функции может быть глобальной, тогда она может существовать за пределы функции
# nonlocal - заставляет идентификатор обратиться к ранее связанной переменной в ближайшей области видимости. Будет видна в этой функции и на один уровень выше.
# g_var = 0
# nl_var = 0
# print('top level -> g_var: {}, nl_var: {}'.format(g_var, nl_var))


# def test():
#     nl_var = 2
#     print('in test -> g_var: {}, nl_var: {}'.format(g_var, nl_var))

#     def inner_test():
#         global g_var
#         nonlocal nl_var
#         g_var = 1
#         nl_var = 4
#         print('in inner -> g_var: {}, nl_var: {}'.format(g_var, nl_var))
#     inner_test()
#     print('in test -> g_var: {}, nl_var: {}'.format(g_var, nl_var))


# test()
# print('in test -> g_var: {}, nl_var: {}'.format(g_var, nl_var))

# присваивание функции к переменной
# функции как любые другие объекты в python можно присвоить к переменной
# def f_to_kelvin(degress_f):
#     return 273.15 + (degress_f - 32) * 5 / 9


# def c_to_kelvin(degress_c):
#     return 273.15 + degress_c


# abs_teperature = f_to_kelvin
# print(abs_teperature(32))
# abs_teperature = c_to_kelvin
# print(abs_teperature(0))

# Лямбда-функции (lambda)
# Позволяет более локанично записывать код функции.
# Преимущества функции
# 1. Синтаксис лямбд экономит пространство в коде
# 2. lambda вместо def
# 3. не используется название функции
# 4. аргументы без скобок
# 5. используется только одно выражение и оно возращается
# 6. лямбда назывется анонимными функциями
# func = lambda x, y: x**y
# print(func(1, 4))

# print((lambda x: x**4)(1))

# Декораторы (@)
# Декоратор - позволяет упаковать одну функцию внутри другой всего в одной строке.
# Использование декоратора состоит из двух частей:
# 1) определить функцию, которая будет включать или декорировать другие функции
# 2) поставить знак @ с декоратором перед определением упаковываемой функции
# Функция декоратор должна получать функцию в параметре и возращать функцию
# Декораторы часто используются в веб-фреймворках (Django), в графических библиотеках
# def getTalk(type='shout'):
#     def shout(word='ga'):
#         # первый символ в верхнем регистре
#         return word.capitalize() + '!'

#     def whisper(word='ga'):
#         return word.lower() + '...'
#     if type != 'shout':
#         return shout()
#     else:
#         return whisper()


# talk = getTalk()
# print(talk)

# функция бутерброт
def bread(func):
    def wrapper():
        print('</___\>')
        func()
        print('<\___/>')
    return wrapper


def ingredients(func):
    def wrapper():
        print('помидор')
        func()
        print('сыр')
    return wrapper


def meat(food='котлета'):
    print(food)


test = ingredients(meat)
gandwich = bread(test)
gandwich()


@bread
@ingredients
def meat(food='котлета'):
    print(food)


meat()
