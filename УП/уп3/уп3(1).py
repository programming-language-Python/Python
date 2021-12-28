a=float(input("Число A: "))
b=float(input("Число B: "))
if a<b:
    while a<=b:
        print(a**3)
        a+=1
else: 
    print("Число A должно быть больше числа B")