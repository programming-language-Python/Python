def quicksort(array):
    if len(array) < 2:
        return array # Базовый случай: массивы с 0 и 1 элементов уже отсортированы
    else: 
        pivot = array[0] # рекрусивный случай
        less = [i for i in array[1:] if i <=pivot] # под массив всех элементов, меньших опорного
        greater = [ i for i in array [ 1: ] if i > pivot] # под массив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)
print (quicksort([10, 5, 2, 3]))