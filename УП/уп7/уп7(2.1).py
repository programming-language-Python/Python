# Для заданных чисел values и среднего значения mean напишите такой filter, который оставляет только элементы больше среднего значения.
values = [4, 8, 15, 16, 23, 42]
mean = 18


def filter(values, mean):
    values_max = []
    for value in values:
        if value > mean:
            values_max.append(value)
    return values_max


# result = [value for value in values if value > mean]
# result = [lambda values, mean: for value in values: if values > mean: ]
result = filter(values, mean)
print(result)
