date = int(input('Введите день: '))
prew = cur = 1
n = 2
while date > n:
    tmp = prew + cur
    prew = cur
    cur = tmp
    print(cur)
    n += 1
sum = 0
for i in str(cur):
    sum += int(i)
print(sum, 'минуты')

if sum > 60:
    print('Машинист отказывается ехать')

# Фибоначи
# number = int(input('Введите натуральное число: '))
# prew = cur = 1
# for n in range(int(number-2)):
#     tmp = prew + cur
#     prew = cur
#     cur = tmp
#     print (cur)
