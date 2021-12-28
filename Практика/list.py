l=list()
p=''
while p!="good":
    p=input("Введите символ для списка. При завершении напишите good: ")
    if p!="good":
        l.append (p)
print(l)