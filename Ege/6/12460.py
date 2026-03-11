from turtle import *

tracer(0)
screensize(10000,10000)
m=20

lt(90)
for i in range(3):
    down()
    for _ in range(2):
        fd(7*m)
        rt(90)
        fd(7*m)
        rt(90)
    up()
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#28+48=76