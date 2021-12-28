# assert утверждение. Использовается для предположении чего-либо
"""def exc(text):
    assert text!=''
    print(str(text))
exc('')
# выбросит исключение AssertionError

def test(number):
    assert number>0, "Number should be bigger than 0."
    # После запятой записывается почему ошибка(описание), т.е. AssertionError: Number should be bigger than 0.
    print(str(number))
test(-10)

# Файлы

file=open('test.txt','r') # возращает дискриптор открытого файла
# по умолчанию стоит режим чтения
print(file.read()) # read() читает всю информацию из файла
file.close() # закрывает файл. Закрываем, чтобы не занимать память
"""
"""
имеет два аргуметна: 
1. Название файла
2. Режим чтения файла (3 основных: r чтение файла, w перезапись файла, a добавление в файл.
Дополнительный: b Binary mode(режим бинарный))
"""
"""
# r
filename=input('Укажите файл ')
file=open(filename,'r')
print("В данном файле",str(len(file.read())),"символов") # len считает (если .txt) количество бит в файле
file.close()
"""
"""
filename=input('Укажите файл ')
file=open(filename,'r')
print(file.read(2)) # в read можно ввести аргумент. Это будет количесвто байтов, которое нужно будет прочитать
print(file.read(2)) # т.к. выше указывали байты, то он продолжит выводить (т.е. выведет 3 и 4 байт)
file.close()
# понадобится, когда не будет хватать оперативной памяти
"""
"""
# w
filename=input('Введите имя файла ')
text=input('Введите содержимое файла ')
file=open(filename,'w')
file.write(text) # .write записывает информацию в файл. Если есть такой файл то его перезаписывает
file.close()
"""
"""
# a
filename=input('Введите имя файла ')
file=open(filename, 'a')
file.write(' TEST ')
file.close()

b Binary mode (режим бинарный) нужен, чтобы считывать с помощью python изображения, музыкальные файлы и т.д.
"""
# Программа для копирования файлов
"""
file1=input('Введите название копируемого файла: ')
file2=input('Введите куда скопировать файл: ')

first_file1=open(file1, 'r')
first_file2=open(file2, 'w')

first_file2.write(first_file1.read())
first_file1.close()
first_file2.close()
print('Копирование успешно завершено!')


file1=input('Какой файл забэкапить?: ')
file2='backup_'+file1

first_file1=open(file1, 'r')
first_file2=open(file2, 'w')

first_file2.write(first_file1.read())
first_file1.close()
first_file2.close()
print('Бэкап успешно завершено!')

# бэкап изображений (b Binary mode). Копирует(бэкапит) и текстовые файлы.
file1=input('Какой файл забэкапить?: ')
file2='backup_'+file1

first_file1=open(file1, 'rb') # просто добавили b. Лучше всегда добавлять b
first_file2=open(file2, 'wb')

first_file2.write(first_file1.read())
first_file1.close()
first_file2.close()
print('Бэкап успешно завершено!')
"""
# Как читать строки?
file = open('C:\\Users\maks2\Desktop\PYTHON\Хауди Хо\Коды_из_видео\stroka.txt','r')
strings=file.readlines() # выводит список строк
print(strings)
for string in strings:
    print(string,end='')
file.close()
"""
# with - перев. с помощью
with open('stroka.txt','r') as f: # помогает совершить точно что при выполнении этого блока файл закроется. f временная переменная.
    print(f.read(5))

если написать 
print(f.read(5))
а потом
print(f.read()) 
то он считывает всё до конца
"""