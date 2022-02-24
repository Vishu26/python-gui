import turtle
import numpy as np
import datetime

s = turtle.getscreen()
s.clearscreen()
s.tracer(False)
t = turtle.Turtle()
t.hideturtle()
t.speed('fastest')
t.pen(fillcolor="#D3D3D3", pensize=2)
t.dot(10)
t.penup()
t.right(90)
t.forward(200)
t.left(90)
t.pendown()
t.circle(200)
t.left(90)
t.penup()
t.forward(10)
t.pendown()
t.right(90)
t.begin_fill()
t.circle(190)
t.left(90)
t.penup()
t.forward(15)
t.pendown()
t.right(90)
t.circle(175)
t.end_fill()
t.left(90)
t.penup()
t.forward(60)
t.pendown()
t.right(90)
t.circle(115)
t.left(90)
t.penup()
t.forward(5)
t.pendown()
t.right(90)
t.circle(110)
s.update()
t.penup()
t.home()
t.pendown()


for i in range(0, 360, 3):
    rad = (np.pi / 2) - (np.pi * i / 180)
    t.penup()
    t.goto(190 * np.cos(rad), 190 * np.sin(rad))
    t.pendown()
    if i%15==0:
        t.goto(175 * np.cos(rad), 175 * np.sin(rad))
        t.penup()
        t.home()
        t.goto(140 * np.cos(rad), 140 * np.sin(rad))
        #t.right(180)
        #t.forward(10)
        t.right(90)
        t.forward(20)
        t.pendown()
        if i%30==0:
            if i==0:    
                t.write("12", align='center', font=('Arial', 32, 'normal'))
            elif i<300:
                #t.color("white")
                #t.write("0", align='center', font=('Arial', 32, 'normal'))
                #t.color("black")
                t.penup()
                t.left(90)
                t.forward(2)
                t.right(90)
                t.forward(5)
                t.pendown()
                t.write(F"{i//30}", align='center', font=('Arial', 32, 'normal'))
            else:
                t.write(F"{i//30}", align='center', font=('Arial', 32, 'normal'))
            t.penup()
            t.goto(190 * np.cos(rad), 190 * np.sin(rad))
            t.pendown()
            t.pen(fillcolor="black")
            t.begin_fill()
            t.goto(200 * np.cos(rad+0.04), 200 * np.sin(rad+0.04))
            t.goto(200 * np.cos(rad-0.04), 200 * np.sin(rad-0.04))
            t.goto(190 * np.cos(rad), 190 * np.sin(rad))
            t.end_fill()
            
        else:
            t.penup()
            t.goto(195 * np.cos(rad), 195 * np.sin(rad))
            t.pendown()
            t.dot(3)

    else:
        t.pen(pensize=1)
        t.penup()
        t.goto(185 * np.cos(rad), 185 * np.sin(rad))
        t.pendown()
        t.goto(180 * np.cos(rad), 180 * np.sin(rad))
        t.pen(pensize=2)

s.update()

hr_hand = turtle.Turtle(visible=False)
min_hand = turtle.Turtle(visible=False)
sec_hand = turtle.Turtle(visible=False)

hr_hand.speed('fastest')
min_hand.speed('fastest')
sec_hand.speed('fastest')

hr_hand.pen(pensize=3)
min_hand.pen(pensize=3)
sec_hand.pen(pensize=3)

while True:

    sec_hand.home()
    min_hand.home()
    hr_hand.home()

    sec_hand.clear()
    min_hand.clear()
    hr_hand.clear()

    time = datetime.datetime.now()
    sec_rad = (np.pi / 2) - (np.pi * (time.second * 6) / 180)
    min_rad = (np.pi / 2) - (np.pi * (time.minute * 6) / 180)
    hr_rad = (np.pi / 2) - (np.pi * (time.hour * 30) / 180) - (np.pi * (time.minute // 2) / 180)

    sec_hand.goto(90 * np.cos(sec_rad), 90 * np.sin(sec_rad))
    min_hand.goto(70 * np.cos(min_rad), 70 * np.sin(min_rad))
    hr_hand.goto(40 * np.cos(hr_rad), 40 * np.sin(hr_rad))

    s.update()

s._root.mainloop()