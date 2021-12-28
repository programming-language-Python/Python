# Измерение времени выполнения кода.
# Есть ещё способ с line_profiler
import time
start_time = time.time() 
# ваш код
time = time.time()-start_time # // время выполнения также будет в секундах
print (time)
#ИЛИ
'''
import timeit

code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""
# .timeit 1 аргумент - код, который хотите проверить,
# 2 аргумент - сколько раз повторять тест
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time) #измеряется в секундах
'''
