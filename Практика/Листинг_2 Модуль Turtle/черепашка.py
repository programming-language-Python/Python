'''
import turtle
t = turtle.Pen()
t.forward(50) # Kоманда forward служит для перемещения черепашки вперед.

t.left(90) # повернем черепашку на 90 градусов влево, введя такую команду.

# квадрат
import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# Чтобы очистить холст, введите команду reset или clear.
# t.reset()
# t.clear()
# перемещать назад командой backward.
# Еще есть команда up, убирающая перо с холста. С помощью команды down рисование можно снова включить.

import turtle
t = turtle.Pen()
t.backward(100)     # назад
t.up()              # поднялось перо
t.right(90)         # поворот пера
t.forward(20)       # смещение вниз
t.left(90)          # поворот пера
t.down()            # перо опустилось
t.forward(100)      # рисование вперед
'''
import turtle
t = turtle.Pen()
t.backward(100)     
t.up()              
t.right(90)         
t.forward(20)       
t.left(90)          
t.down()
t.fillcolor("yellow")  # черепашка стала желтой
t.stamp()              # черепешка шлепнулась. Оставляет стрелку и появляется (спам) черепашка, которая передвигается.
t.pencolor("orange")   # черепашка рисует рыжим. Полосы оставляет.
t.shape("turtle")      # появилась настоящая черепашка
t.forward(100)

'''
import turtle

t = turtle.Pen()
t.screen.setup(800, 800)       # задаем размер холста
t.up()
t.goto(-450, 0)                # перемещаем в начальную точку
t.down()         
t.setheading(270)              # угол поворота в градусах относительно начального положения черепашки

for i in range(5):             # цикл рисования 
    if 2>= i >=1 :
        t.fillcolor("tomato")  # закрашивания фигуры указанным цветом 
    elif i>2:
        t.fillcolor("lime")
    t.circle(50, 180)          # рисование окружности. t.circle(r, ϕ), где r – радиус круга, ϕ – часть окружности
    t.begin_fill()             # закрашивания фигуры цветом черепашки
    t.circle(-50, 180)      
    t.end_fill() 
     
t.screen.mainloop()            # останавливает выполнение программы. После завершения программы оставляет окно открытой.

d= int(input('Число определения частей круга: '))
r= int(input('Радиус курогов: '))
rBig= int(input('Радиус большого курга: '))
import turtle, random

color_list=['mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'limegreen', 'darkgreen', 'yellow', 'darkorange', 'orange']

t = turtle.Pen()
t.screen.setup(800, 800)

def circ(d, r, rBig):
    for i in range(d):
        c = random.choice(color_list)     # рандомный цвет из списка
        t.circle(rBig, 360/d)           # рисование окружности. rBig-радиус круга, 360/d - колличество частей круга
        t.dot(r, c)                       # рисование точки. t.dot(r, color), где r–радиус точки в пикселях, color–цвет точки
        
t.up()
t.goto(350, 0)                            # перемещаем в начальную точку
t.setheading(90)                          # угол поворота в градусах относительно начального положения черепашки
t.down()

#circ(40, 10, 200) 
circ(d, r, rBig)                         # передаем параметры функции
t.screen.mainloop() 

import turtle

def drawMulticolorSqure(t,sz):
    # создание крадрата с помощью цикла
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)      # длина сторон
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('black')   # цвет холста

alex = turtle.Turtle()
alex.pensize(3)            # размер пера

size = 20
for i in range(15):
    drawMulticolorSqure(alex,size)
    size = size + 10
    alex.forward(10)
    alex.right(18) # 90 прикольно

import turtle

colors=['red', 'purple', 'blue','green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('black') # цвет фона
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1) # width - ширина
    t.forward(x)
    t.left(59)
    t.speed(-1)  # скорость рисования, где 1-медленно, 10-быстро
    '''