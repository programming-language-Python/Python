shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаём копию путём полной вырезки. Если убрать вырезку то они будут одинаковые
del mylist[0] # удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist) # Обратите внимание, что теперь списки разные