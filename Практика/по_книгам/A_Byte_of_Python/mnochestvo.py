'''
Множества –это неупорядоченные наборы
простых объектов. Они необходимы тогда,
когда присутствие объекта в наборе важнее 
порядка или того, сколько раз данный
объект там встречается.
Используя множества, можно осуществлять
проверку принадлежности, определять,
является ли данное множество
подмножеством другого множества,
находить пересечения множеств и так далее.
'''
bri = set(['Бразилия', 'Россия', 'Индия'])
print (bri)
bric=bri.copy()
'''print(bric)
bric.add('Китай')
print(bric)'''
print (bric.issuperset(bri))
'''
print(bri.remove('Россия'))
print(bri & bric) # OR bri.intersection(bric)
'''