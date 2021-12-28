age=26
name= 'Rom'
print('Возраст {0}--{1} лет'.format(name,age))
print('Имя ваше {0} '.format(name))
''' 
ИЛИ
age=26
name= 'Rom'
print('Возраст {}--{} лет'.format(name,age))
print('Имя ваше {} '.format(name))
'''
# десятичное число (.) с точностью в 3 знака для плавающих
print('{0:.3}'.format(1/3)) #0.333
# заполнить подчёркиваниями (_) с центровкой текста (^) по шинине 11:
print('{0:_^11}'.format('hello')) # __hello__
# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python')) # Swaroop написал A Byte of Python