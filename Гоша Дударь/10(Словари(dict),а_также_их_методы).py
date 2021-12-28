# словари
# примеры записи словарей (5 примера)
d={'short':'dict', 'longer':'dictionary'}
d1=dict(short='dict', longer='dictionary')
d2=dict([(23,24),(56,87)])
d3= dict.fromkeys (['a','b','c'],1) # всем значением присвоит 1
d4={a:a**2 for a in range (7)} # с помощью цикла
print (d)
print (d1)
print (d2)
print (d3)
print (d4)