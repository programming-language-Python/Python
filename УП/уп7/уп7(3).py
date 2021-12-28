import turtle, random
t = turtle.Pen()
t.screen.setup(800, 800)
t.up()
t.goto(-200, 0)
t.right(90)
t.down()

# треугольник
t.fillcolor("lime")
t.begin_fill() # begin
t.forward(300)
t.left(90)
t.forward(300)
t.left(135)
t.forward(425)
t.end_fill() # end

t.up()

# треугольники=ромб:
colors=['red', 'purple', 'blue','green', 'yellow', 'orange','mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'limegreen', 'darkgreen','darkorange']
c=random.choice(colors)
# расположение
t.left(135)
t.forward(235) # вертикаль
t.left(90)
t.forward(80) # горизонт
t.left(150)
t.down()
# фигура 
for k in range(2):
    for j in range(4):
        c=random.choice(colors)
        t.fillcolor(c)
        t.left(360/4)
        t.begin_fill() # begin
        for i in range(3):
            t.forward(60)
            t.left(120)
        t.end_fill() # end
    t.right(45)         
t.left(45)

# звезда
t.up()
t.left(-105)
t.forward(100)
t.left(60)

t.down()
t.fillcolor('Purple')
t.begin_fill() # begin
for k in range(6):
    t.speed(1)
    t.forward(20)
    t.right(120)
    t.forward(20)
    t.left(60)
t.end_fill() # end

t.speed(10)
# круг
t.up()
t.fillcolor("yellow")
t.goto(-175, -170)
t.forward(100)
t.left(90)
t.forward(30)
t.down()
t.begin_fill()
t.stamp()
t.shape("turtle")
t.circle(25,360)
t.end_fill()

t.screen.mainloop()