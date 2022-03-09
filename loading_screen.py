import turtle
import numpy as np

s = turtle.getscreen()
s.clearscreen()
s.tracer(False)
t = turtle.Turtle()
t.hideturtle()
t.speed('fastest')
l = turtle.Turtle()
l.hideturtle()
l.speed('fastest')
cols = ["#ffffff", "#e5e5e5", "#cbcbcb", "#b2b2b2", "#9a9a9a",
"#828282", "#6c6c6c", "#565656", "#404040", "#2c2c2c", "#1a1a1a",
"#000000"]

load = ["Loading .  ", "Loading .. ", "Loading ..."]

while True:
    l.clear()
    for i in enumerate(range(0, 360, 30)):
        rad = (np.pi / 2) - (np.pi * i[1] / 180)
        t.penup()
        t.goto(120 * np.cos(rad), 120 * np.sin(rad))
        t.pendown()
        t.pen(fillcolor=cols[i[0]], pencolor=cols[i[0]])
        t.begin_fill()
        t.circle(20)
        t.end_fill()
    l.penup()
    l.goto(0, -200)
    l.pendown()
    l.pen(pencolor="#000")
    l.write(load[0], align='center', font=('Arial', 32, 'normal'))
    cols = np.roll(cols, 1)
    load = np.roll(load, -1)
    s.update()

s._root.mainloop()