try:
    x=int(input())
except ValueError:
    print('Вы ввели не число ')
else: # если нет исключения
    print ('Всё верно')
finally: # выводится всегда
    print ('Завершение')