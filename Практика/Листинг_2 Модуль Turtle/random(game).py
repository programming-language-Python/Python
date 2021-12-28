import random
num = random.randint(1, 29)
print (num)
while True:
    print ( 'Угадайте число от 1 до 100' )
    i = int(input())
    
    if i == num:
        print( 'Правильно! ' )
        break
    elif i < num:
        print( 'Загаданное число больше')
    elif i > num:
        print( 'Загаданное число меньше')