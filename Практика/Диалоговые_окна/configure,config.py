# Виджеты могут быть сконфигурированы во время создания, но иногда необходимо изменить
# конфигурацию виджета во время исполнения программы. Для этого используется метод configure
# (или его синоним config). Также можно использовать квадратные скобки (widget['option'] = new_value).
# Пример, программа выводит текущее время, после клика по кнопке:
from tkinter import *
import time
def button_clicked():
    # изменяем текст кнопки
    button['text'] = time.strftime('%H:%M:%S')
root=Tk()
# создаём виджет
button = Button(root) # можно без root
# конфигурируем виджет после создания
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
# также можно использовать квадратные скобки:
# button['text'] = time.strftime('%H:%M:%S')
# button['command'] = button_clicked
button.pack()
root.mainloop()



