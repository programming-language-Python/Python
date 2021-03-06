# Виджет отображает уровень загрузки.

# length - длина полосы.
# start
# Запускает бесконечный цикл загрузки. Шаг длиною 1 выполняется один раз в указанное время (в миллисекундах).

# stop
# Останавливает цикл загрузки.

# step
# Продвигает загрузку на заданное количество шагов.

import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
pb = ttk.Progressbar(root, length=100)
pb.pack()
pb.start(100)
root.mainloop()