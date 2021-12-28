def binary_search(list, item):
    '''
    В переменных low и high хранятся
    границы той части списка, в которой
    выполняется поиск
    '''
    low = 0
    high = len(list)-1
    while low <= high: # Пока эта часть не сократится до одного элемента...
        mid = (low + high) # ...проверяем средний элемент
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
            return None 
my_list = [1, 3, 5, 7, 9] 
print (binary_search(my_list, 3))
print (binary_search(my_list, -1))