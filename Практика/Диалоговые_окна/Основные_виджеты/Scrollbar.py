# Этот виджет даёт возможность пользователю "прокрутить" другой виджет (например текстовое поле) и часто бывает полезен.
# Использование этого виджета достаточно нетривиально. Необходимо сделать две привязки:
# command полосы прокрутки привязываем к методу xview/yview виджета,
# а xscrollcommand/yscrollcommand виджета привязываем к методу set полосы прокрутки.

# Рассмотрим на примере:

from tkinter import *
root = Tk()
text = Text(root, height=3, width=60)
text.pack(side='left')
scrollbar = Scrollbar(root)
scrollbar.pack(side='left')
# первая привязка
scrollbar['command'] = text.yview
# вторая привязка
text['yscrollcommand'] = scrollbar.set
root.mainloop()