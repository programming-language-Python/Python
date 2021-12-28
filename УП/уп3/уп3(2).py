a = float(input("Число A: "))
b = float(input("Число B: "))
c = float(input("Число C: "))
if a + b == c:
    print("Получилось")
elif a + c == b:
    print("Получилось")
elif b + c == a:
    print("Получилось")
else:
    print("Не получилось")
