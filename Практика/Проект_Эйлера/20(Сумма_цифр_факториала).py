def fact(n):
# Возвращает факториал заданного числа.
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r
s=fact(1000)
s=str(s)
k=[]
for i in range(len(s)):
    k.append(int(s[i]))
print(sum(k))