'''
Функция exec служит для выполнения
команд Python, содержащихся в строке
или файле, в отличие от самого текста
программы. Например, во время выполнения
программы можно сформировать строку,
содержащую текст программы на Python,
и запустить его при помощи exec.
''' 
exec('print("Здравствуй, Мир!")')
'''
Аналогично, функция eval позволяет
вычислять корректные выражения Python,
содержащиеся в строке.
'''
print(eval('2*3'))