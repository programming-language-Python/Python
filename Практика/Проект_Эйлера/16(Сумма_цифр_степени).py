'''
s=pow(2,1000)
s=str(s)
k=0
for i in range(len(s)):
    k+=int(s[i])
print(k)
'''
s=pow(2,1000)
s=str(s)
k=[]
for i in range(len(s)):
    k.append(int(s[i]))
print(sum(k))

