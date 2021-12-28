# Составьте функцию max3(), получающую три аргумента типа int ли float и возвращающую наибольший из них.
def max3(a, b, c):
    max = 0
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    return max


print(max3(1, 2, 3))
