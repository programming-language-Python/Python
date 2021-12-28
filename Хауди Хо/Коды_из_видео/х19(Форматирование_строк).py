# %
'''
name="Джесси"
age=21
print('Привет, %s!\nТебе уже %d год!'% (name, age))
# %s=name %d=age
# s - Плейсхолдер строка
# %d - Плейсхолдер числа
# %f - Плейсхолдер дроби
# Метод .format()
print('Привет, {}!\nТебе уже {} год!'.format(name, age))
print('{0}{1}{0}'.format('abra','cad'))
print('Привет, {person_name}!\nТебе уже {person_age} год!'.format(person_name=name,person_age=age))

pesron={'name':'Jessy', 'age':21} # словарь
print('Имя: {name}\nВозраст: {age}'.format(name=pesron['name'],age=pesron['age']))

human={'name':'Jessy', 'age':21}
print('Имя: {p[name]}\nВозраст: {p[age]}'.format(p=human))
'''


'''
****Jessy****
____Jessy____
___Jonatan___
sdfffghgjhjjk
adsadawdeaed_
'''
input_str='Jessy'
print('{0:*^10}'.format(input_str))
print('{0:*<11}'.format(input_str))
print('{0:*>15}'.format(input_str))
print('{0:>15}'.format(input_str))
print('{0:_>15}'.format(input_str))
'''
1 аргумент (не считая 0) это символ заполнитель. 
2 аргумент направление заполнения (если не ставить то по умолчанию будет пробел): 
левое - Jessy***** (<), правое - *****Jessy(>), центрированное -  **Jessy*** (^)
3 аргумент это количество знаков мест в которой нужно местить эту строку
'''
# программа, которая ставит равное количество символов
lenght=10
if len(input_str) % 2: # если есть остаток то True
    lenght+=1
print(('{0:*^'+str(lenght)+'}').format(input_str))