def func(a, b=5, c=10):# пррсто c не считается значением по умолчанию
    print('a равно', a, ', b равно', b, ', а c равно', c) 
func(3, 7) 
func(25, c=24) 
func(c=50, a=100) # так пишутся только если заданно значение по умолчанию

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
         count += keywords[key] 
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100)) 
# initail=10, numbers=[1,2,3],  keywords=50,100