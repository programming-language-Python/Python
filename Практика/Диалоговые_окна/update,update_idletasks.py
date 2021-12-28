# Две функции, для работы с очередью задач. Их выполнение вызывает обработку отложенных задач.
# update_idletasks выполняет задачи, обычно откладываемые "на потом", когда приложение будет простаивать.
# Это приводит к прорисовке всех виджетов, расчёту их расположения и т.д. Обычно эта функция используется
# если были внесены изменения в состояние приложения, и вы хотите, чтобы эти изменения были отображены
# на экране немедленно, не дожидаясь завершения сценария.

# update обрабатывает все задачи, стоящие в очереди. Обычно эта функция используется во время "тяжёлых" расчётов,
# когда необходимо чтобы приложение оставалось отзывчивым на действия пользователя.
# Пример:
from tkinter import *
import math
def hard_job():
    x = 1000
    while True:
        x = math.log(x) ** 2.8
        root.update()
root=Tk()
button = Button()
button.pack()
root.after(500, hard_job)
root.mainloop()