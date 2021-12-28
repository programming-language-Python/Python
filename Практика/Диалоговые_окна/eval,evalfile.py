# Две недокументированные функции для выполнения кода на tcl.
# eval позволяет выполнить строку на языке программирования tcl,
# а evalfile - выполнить код, записанный в файл.
# В качестве аргументов принимают соответственно строку и путь к файлу.
# Данные функции полезны при использовании дополнительных модулей, написанных на tcl. Пример:

from tkinter import *
root=Tk()
root.eval('package require tile; ttk::style theme use clam')
root.eval('ttk::button .b -text {ttk button}; pack .b')
root.mainloop()