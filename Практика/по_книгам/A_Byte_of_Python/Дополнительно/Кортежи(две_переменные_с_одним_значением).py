def get_error_details():
    return (2, 'описание ошибки No2')
errnum, errstr = get_error_details() 
print(errnum)
print(errstr)

a, *b = [1, 2, 3, 4]
print(a)
print(b)

# меняем значения местами
a = 5; b = 8
a, b = b, a
print(a,b)