import numpy as np
matrix = input('Введите числа в матрицу 3x3 через пробел: ').split(' ')
while len(matrix) < 9:
    matrix = input('Введите числа в матрицу через пробел!!!: ').split(' ')
matrix = [matrix[0:3], matrix[3:6], matrix[6:9]]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
min_str = []  # список с минимальными числами строк
for i in matrix:
    min_str.append(min(i))
max_str = max(min_str)  # максимальное число из min_str

arr = np.array(matrix)  # преобразование в массив
print(arr)
size = len(matrix[0])
max_column = []  # список с максимальными числами столбцов
for j in range(size):
    max_column.append(max(arr[:, j]))
min_column = min(max_column)  # минимальное число в max_column

if max_str == min_column:
    print('Good and True')
else:
    print('Badly and False')
