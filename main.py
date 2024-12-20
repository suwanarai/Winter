import turtle


screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("light blue")

t = turtle.Turtle()
t.hideturtle()
t2 = turtle.Turtle()
t2.hideturtle()

t_ground =turtle.Turtle()
t_ground.fillcolor('snow1')
t_ground.pencolor('snow1')
t_ground.speed(0)
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

t.penup()
t.goto(50,-100)
t.pencolor('black')
t.fillcolor('white')
t.pendown()
t.begin_fill()
t.circle(75)
t.end_fill()

t.penup()
t.goto(50,45)
t.pencolor('black')
t.fillcolor('white')
t.pendown()
t.begin_fill()
t.circle(60)
t.end_fill()

t.penup()
t.goto(50,150)
t.pencolor('black')
t.fillcolor('white')
t.pendown()
t.begin_fill()
t.circle(55)
t.end_fill()

t.penup()
t.goto(75,200)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(40,200)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(50,160)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(40,160)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(60,160)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(70,165)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(30,165)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.hideturtle()
t.pencolor('green')
t.fillcolor('green')
t.penup()
t.goto(60,50)#1/4
t.pendown()
t.begin_fill()
t.goto(140,50)
t.goto(100,150)
t.goto(60,50)
t.end_fill()

t.penup()
t.goto(55,30)#1/4
t.pendown()
t.begin_fill()
t.goto(145,30)
t.goto(100,130)
t.goto(55,30)
t.end_fill()

t.penup()
t.goto(45,10)#1/4
t.pendown()
t.begin_fill()
t.goto(155,10)
t.goto(100,110)
t.goto(45,10)
t.end_fill()

t.penup()
t.goto(40,-10)#1/4
t.pendown()
t.begin_fill()
t.goto(160,-10)
t.goto(100,110)
t.goto(40,-10)
t.end_fill()

t.penup()
t.goto(30,-30)#1/4
t.pendown()
t.begin_fill()
t.goto(170,-30)
t.goto(100,90)
t.goto(30,-30)
t.end_fill()

t.penup()
t.goto(20,-50)#1/4
t.pendown()
t.begin_fill()
t.goto(180,-50)
t.goto(100,70)
t.goto(20,-50)
t.end_fill()

t.penup()
t.goto(10,-70)#1/4
t.pendown()
t.begin_fill()
t.goto(190,-70)
t.goto(100,50)
t.goto(10,-70)
t.end_fill()

t.penup()
t.goto(0,-90)#1/4
t.pendown()
t.begin_fill()
t.goto(200,-90)
t.goto(100,30)
t.goto(0,-90)
t.end_fill()

t.penup()
t.pencolor('chocolate4')
t.goto(90, -110)
t.fillcolor('chocolate4')
t.pendown()
t.begin_fill()
t.forward(10)
t.left(90)
t.forward(20)
t.left(90)
t.forward(10)
t.left(90)
t.forward(20)
t.end_fill()

t.penup()
t.goto(150, -100)
t.fillcolor('red')
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.end_fill()

t.penup()
t.goto(200, -90)
t.fillcolor('yellow')
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(15)
t.left(90)
t.forward(50)
t.left(90)
t.forward(15)
t.end_fill()

t.pencolor('red')
t.pensize(2)
t.penup()
t.goto(190,-80)
t.pendown()
t.circle(10)
t.penup()

t.pencolor('red')
t.pensize(2)
t.penup()
t.goto(180,-80)
t.pendown()
t.circle(10)
t.penup()

t.pencolor("goldenrod3")
t.fillcolor("gold1")
t.penup()
t.begin_fill()
t.goto(-30,220)
t.pendown()
t.goto(30,220)
t.goto(-20,190)
t.goto(0,240)
t.goto(20,190)
t.goto(-30,220)
t.end_fill()

t.penup()
t.goto(100,110)
t.pencolor('Blue')
t.fillcolor('Blue')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(110,120)
t.pencolor('red')
t.fillcolor('red')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(120,105)
t.pencolor('purple')
t.fillcolor('purple')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(150,160)
t.pendown()
t.write("Merry Christmas",font=("Calibri",14,"bold italic"),align="center")

#cloud
t.goto(0,300)
t.pencolor('white')
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.goto(-55,285)
t.circle(40)
t.goto(45,285)
t.circle(40)
t.end_fill()
t.penup()










#this is last line of code
turtle.done()












