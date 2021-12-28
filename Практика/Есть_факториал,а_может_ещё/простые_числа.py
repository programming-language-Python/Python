n = int ( input ("Введите число n: "))
for a in range (2, n):
    if (n % a) == 0:
        print ("Число ", n, "не простое")
        break
    elif (n // a) == 1:
        print ("Число ", n, " простое!")
        break