import turtle
t = turtle.Pen()
t.screen.setup(800, 800)
t.up()
t.goto(-400,0) # 1 аргумент горизонт, 2 аргумент вертикаль. Получается если от -400 до 400 то это 800
for i in range(9):
    if i//3>0:
        t.fillcolor("lime")
    else:
        t.fillcolor("blue")
    t.forward(70)
    t.down()
    t.begin_fill() # t.begin_fill() и t.end_fill() показывают интервал закраски
    for j in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()
    t.up()
    # круг fail
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.down()
    t.circle(5,3)
    t.speed(1)