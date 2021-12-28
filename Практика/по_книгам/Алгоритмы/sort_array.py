# сортировка массива по возрастанию
# функция нахождения наименьшего числа начиная с индекса 1
'''def Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
# функция сортировки
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print (Smallest([5,3,6,2,10]))
print (selectionSort([5,3,6,2,10])) 
'''
# сортировка массива по убыванию
# функция нахождения наибольшего числа начиная с индекса 1
def Smallest2(arr):
    smallest2 = arr[0]
    smallest2_index = 0
    for i in range(1, len(arr)):
        if arr[i] > smallest2:
            smallest2 = arr[i]
            smallest2_index = i
    return smallest2_index
# функция сортировки
def selectionSort2(arr):
    newArr = []
    for i in range(len(arr)):
        smallest2 = Smallest2(arr)
        newArr.append(arr.pop(smallest2))
    return newArr
print (Smallest2([5,3,6,2,10]))
print (selectionSort2([5,3,6,2,10]))

