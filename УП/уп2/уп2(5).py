a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
d = float(input("D: "))
e = float(input("E: "))
# col=[abs(a-b),abs(a-c),abs(a-d),abs(a-e)]
# Определение самой близкой точки к точке A
if abs(a - b) < abs(a - c) and abs(a - b) < abs(a - d) and abs(a - b) < abs(a - e):
    print("Точка B расположена ближе к точке A\nРасстояние точки B до точки A = " + str(abs(a - b)))
elif abs(a - c) < abs(a - b) and abs(a - c) < abs(a - d) and abs(a - c) < abs(a - e):
    print("Точка C расположена ближе к точке A\nРасстояние точки C до точки A = " + str(abs(a - c)))
elif abs(a - d) < abs(a - b) and abs(a - d) < abs(a - c) and abs(a - d) < abs(a - e):
    print("Точка D расположена ближе к точке A\nРасстояние точки D до точки A = " + str(abs(a - d)))
elif abs(a - e) < abs(a - b) and abs(a - e) < abs(a - c) and abs(a - e) < abs(a - d):
    print("Точка E расположена ближе к точке A\nРасстояние точки E до точки A = " + str(abs(a - e)))
# Определение самой дальной точки к точке A
if abs(a - b) > abs(a - c) and abs(a - b) > abs(a - d) and abs(a - b) > abs(a - e):
    print("B самая дальняя точка расстояние до точки A " + str(abs(a - b)))
elif abs(a - c) > abs(a - b) and abs(a - c) > abs(a - d) and abs(a - c) > abs(a - e):
    print("C самая дальняя точка расстояние до точки A " + str(abs(a - c)))
elif abs(a - d) > abs(a - b) and abs(a - d) > abs(a - c) and abs(a - d) > abs(a - e):
    print("D самая дальняя точка расстояние до точки A " + str(abs(a - d)))
elif abs(a - e) > abs(a - b) and abs(a - e) > abs(a - c) and abs(a - e) > abs(a - d):
    print("E самая дальняя точка расстояние до точки A " + str(abs(a - e)))
# m = max(col)
# i = col.index(m)
'''
if i==0:
    print("B самая дальняя точка " + str(m))
elif i==1:
    print("C самая дальняя точка " + str(m))
elif i==2:
    print("D самая дальняя точка " + str(m))
elif i==3:
    print("E самая дальняя точка " + str(m))
'''
