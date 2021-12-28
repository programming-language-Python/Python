'''
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''
# правильный:
import fractions
def compute():
    ans = 1
    for i in range(1, 21):
        # наибольший общий делитель чисел a и b.
        ans *= i // fractions.gcd(i, ans)
    return str(ans)

if __name__ == "__main__":
    print(compute())
'''
# КОД МЕДЛЕННО РАБОТАЕТ!!!
a=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=20
n=0
while j<=20:
    if i%j==0:
        j+=1
    else:
        i+=10
        j=2
print(i)
# ИЛИ
while True:
    for j in a:
        if i%j!=0:
            i+=20
            n=0
            break
        else:
            n+=1
    if n==19:
        print(i)
        break
'''