def summa(list):
    if list==[]:
        return 0
    return list[0]+summa(list[1:])
print (summa([1,2,3,4,5]))