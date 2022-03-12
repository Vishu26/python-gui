import turtle
import numpy as np
from itertools import cycle
from time import sleep

s = turtle.Screen()
s.clearscreen()
s.tracer(False)

t = [turtle.Turtle() for i in range(8)]
for turt in t:
    turt.hideturtle()
    turt.speed('fastest')

base = turtle.Turtle()
base.hideturtle()
base.speed('fastest')

base.penup()
base.right(90)
base.forward(200)
base.left(90)
base.pendown()
base.circle(200)

steps1 = list(range(0, 9)) + list(range(7, 0, -1))
steps2 = [1] + list(range(0, 9)) + list(range(7, 0, -1))
steps3 = [2, 1] + list(range(0, 9)) + list(range(7, 0, -1))
steps4 = [3, 2, 1] + list(range(0, 9)) + list(range(7, 0, -1))
steps5 = [4, 3, 2, 1] + list(range(0, 9)) + list(range(7, 0, -1))
steps6 = [5, 4, 3, 2, 1] + list(range(0, 9)) + list(range(7, 0, -1))
steps7 = [6, 5, 4, 3, 2, 1] + list(range(0, 9)) + list(range(7, 0, -1))
steps8 = [7, 6, 5, 4, 3, 2, 1] + list(range(0, 9)) + list(range(7, 0, -1))

s1, s2, s3, s4, s5, s6, s7, s8 = iter(steps1), iter(steps2), iter(steps3), iter(steps4), iter(steps5), iter(steps6), iter(steps7), iter(steps8)
while True:
    try:
        n1 = next(s1)
    except StopIteration:
        s1 = iter(steps1)
        n1 = next(s1)
    try:
        n2 = next(s2)
    except StopIteration:
        s2 = iter(steps2)
        n2 = next(s2)
    try:
        n3 = next(s3)
    except StopIteration:
        s3 = iter(steps3)
        n3 = next(s3)
    try:
        n4 = next(s4)
    except StopIteration:
        s4 = iter(steps4)
        n4 = next(s4)
    try:
        n5 = next(s5)
    except StopIteration:
        s5 = iter(steps5)
        n5 = next(s5)
    try:
        n6 = next(s6)
    except StopIteration:
        s6 = iter(steps6)
        n6 = next(s6)
    try:
        n7 = next(s7)
    except StopIteration:
        s7 = iter(steps7)
        n7 = next(s7)
    try:
        n8 = next(s8)
    except StopIteration:
        s8 = iter(steps8)
        n8 = next(s8)
    for turt in t:
        turt.clear()
        turt.penup()
    t[0].goto(0, 180 - n1 * 45)
    t[1].goto(180*0.383 - n2*0.383*45, 0.924*180 - n2*0.924*45)
    t[2].goto(90*np.sqrt(2) - n3*np.sqrt(2)*22.5, 90*np.sqrt(2)-n3*np.sqrt(2)*22.5)
    t[3].goto(180*0.924 - n4*0.924*45, 0.383*180 - n4*0.383*45)
    t[4].goto(180 - n5 * 45, 0)
    t[5].goto(180*0.924 - n6*0.924*45, -0.383*180 + n6*0.383*45)
    t[6].goto(90*np.sqrt(2) - n7*np.sqrt(2)*22.5, -90*np.sqrt(2)+n7*np.sqrt(2)*22.5)
    t[7].goto(180*0.383 - n8*0.383*45, -0.924*180 + n8*0.924*45)
    for turt in t:
        turt.pendown()
        turt.circle(10)

    s.update()
    sleep(1)

s._root.mainloop()
