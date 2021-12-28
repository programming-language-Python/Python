l = list()
p = input('Введите числа в список через пробел: ')
l = p.split(' ')  # преобразование из строки в список
print(l)
vod = input("Поиск значения в списке: ")
# if vod in l:
#     print (vod + " есть в списке его индекс "+str(l.index (vod)))
# else:
#     print(vod + " нет в списке")

try:
    if bool(l.index(vod)) == True:
        print(vod + " есть в списке его индекс "+str(l.index(vod)))
except ValueError:
    print(vod + " нет в списке")
