# map. принимает два аргумента: функцию и аргумент составного типа данных, например, список.
def polite_name(name):  
  	 return 'Mr. ' + name     
guests = ["Boris", "Ivan", "Bob"] 
guest_iterator = map(polite_name, guests)
print (list(guest_iterator))

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print (new_list) # из строки превратил в целые числа (integer)