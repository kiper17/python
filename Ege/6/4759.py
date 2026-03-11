from turtle import *

tracer(0)
screensize(1000,1000)
m=20

fd(9*m)
rt(90)
for i in range(2):
    fd(3*m)
    rt(90)
    fd(3*m)
    rt(270)
for i in range(2):
    fd(3*m)
    rt(90)
fd(9*m)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#73