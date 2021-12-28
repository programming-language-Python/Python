num=list(range(101)) # list переводит аргумент в список. Range список из скольких цифр сгенерирует
num1=list(range(50,101)) # range('начало', 'конец')
num2=list(range(1,101,3)) #range('с какого элемента начинать', 'сколько всего символов', 'какой по счёту пропускать символ')
n=[1,2,3,4,5]
i=0
length=len(n)-1
while i<=length:
    print(str(n[i]))
    i+=1
# или
for element in n:
    print(str(element))
print(num2)
for perem in range(15): # 15 раз выведет Hello. Создаём временный массив
    print('Hello!')
for perem in range(1,15,2):
    print('Hello!')