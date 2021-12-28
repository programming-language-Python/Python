"""if 1:
    print("True")
if 0:
    print("True\n") #
    print("All if okay")

if 1:
    print("True\n") # \n переход на новую строку(т.ет enter)
    print("All if okay")
    
num=input("Введите ваше имя: ")    
if num=="Test":
    print("True\n") # \n переход на новую строку(т.ет enter)
    print("All if okay")
    """
"""
num=int(input("Введите число: "))    
if num>0:
    if num > 10:  
        print("Вы ввели число больше 10")
    else:
        print("Вы ввели число меньше 10 и больше 0")
elif num<-10: # используется исключительно с if, т.е. если если if
    print("Вы ввели число меньше -10")
elif num<-100: # используется исключительно с if, т.е. если если if
    print("Вы ввели число меньше -100")
else:
    print("Вы ввели число меньше 0 и больше -10")
print("All if okay")
"""
name=input()
A='Yes' if name !="Test" else "No"
print(A)