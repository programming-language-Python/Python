def kol (list):
    if list==[]:
        return 0
    return 1+kol(list[1:])
print(kol([1,2,3,4,5,6,7]))