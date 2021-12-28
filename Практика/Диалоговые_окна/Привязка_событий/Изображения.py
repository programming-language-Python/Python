# Для работы с изображениями в Tkinter имеется два класса BitmapImage и PhotoImage.
# BitmapImage представляет собой простое двухцветное изображение, PhotoImage - полноцветное изображение.

# BitmapImage
# Конструктор класса принимает следующие аргументы:

# background и foreground - цвета фона и переднего плана для изображения. Поскольку изображение двухцветное,
# то эти параметры определяют соответственно чёрный и белый цвет.
# file и maskfile - пути к файлу с изображением и к маске (изображению, указывающему какие пиксели будут прозрачными).
# data и maskdata - вместо пути к файлу можно указать уже загруженные в память данные изображения.
# Данная возможность удобна для встраивания изображения в программу.
# Пример:

from tkinter import *
data = '''#define image_width 15
#define image_height 15
static unsigned char image_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x1c, 0x30, 0x0c, 0x60, 0x06,
   0x60, 0x06, 0xc0, 0x03, 0xc0, 0x03, 0x60, 0x06, 0x60, 0x06, 0x30, 0x0c,
   0x38, 0x1c, 0x00, 0x00, 0x00, 0x00 };'''
root=Tk()
image = BitmapImage(data=data, background='red', foreground='green')
button=Button(root, image=image)
button.pack()
root.mainloop()
# PhotoImage
# PhotoImage позволяет использовать полноцветное изображение. Кроме того у этого класса есть несколько (достаточно примитивных)
# методов для работы с изображениями. PhotoImage гарантированно понимает формат GIF.

# Аргументы конструктора:

# file - путь к файлу с изображением.
# data - вместо пути к файлу можно указать уже загруженные в память данные изображения.
# Изображения в формате GIF могут быть закодированы с использованием base64.
# Данная возможность удобна для встраивания изображения в программу.
# format - явное указание формата изображения.
# width, height - ширина и высота изображения.
# gamma - коррекция гаммы.
# palette - палитра изображения.