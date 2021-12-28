import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы необходима как минимум \ версия Python 3.0", RuntimeWarning)
else:
    print('Нормальное продолжение')
# warnings служит для отображения предупреждений пользователю.
sys.version_info
(3, 0, 0, 'beta', 2)
print (sys.version_info[0] >= 3)