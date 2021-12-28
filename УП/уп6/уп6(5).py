import numpy as np
# matrix = input('Введите числа в матрицу 4x4 через пробел: ').split(' ')
# while len(matrix) < 16:
#     matrix = input('Введите числа в матрицу через пробел!!!: ').split(' ')
# matrix = [matrix[0:3], matrix[3:6], matrix[6:9], matrix[9:16]]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix)
all_F = []
all_N = []

a = float(input('Доп. коэффициент: '))
b = 1 - a
number1 = 1
for i in matrix:
    F = 'F' + str(number1)
    globals()[F] = max(i) * a + min(i) * b
    all_F.append(globals()[F])
    number1 += 1

arr = np.array(matrix)  # преобразование в массив
size = len(matrix[0])
number1 = 1
for j in range(size):
    N = 'N' + str(number1)
    globals()[N] = max(arr[:, j]) * b + min(arr[:, j]) * b
    all_N.append(globals()[N])
    number1 += 1

number2 = 1
for z in range(size):
    letF = 'F' + str(number2)
    letN = 'N' + str(number2)
    print(globals()[letF], globals()[letN])
    if globals()[letF] == globals()[letN]:
        print('Игра в чистых стратегиях')
    number2 += 1
print('Сумма всех F:', sum(all_F))
print('Сумма всех N:', sum(all_N))
