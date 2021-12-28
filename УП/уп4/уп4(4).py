s =str(input('Введи строку: '))
s=' '+s
print(s)
i=1
t=''
for j in range(len(s)-1):
    if i % 4 == 0:
        i+=1
    else:
        t=t+s[i]
        i+=1
print(t)

# scores = [54,67,48,99,27]
# for i, score in enumerate(scores,1): # условно меняет нумерацию списка 
#    print(i, score)
