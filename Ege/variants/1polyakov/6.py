from turtle import *

tracer(0)
screensize(10000,10000)
m = 15

for i in range(8):
    fd(22*m)
    rt(90)
    fd(33*m)
    rt(90)

up()

bk(8*m)
rt(90)
fd(11*m)
lt(90)

down()

for i in range(8):
    fd(73*m)
    rt(90)
    fd(62*m)
    rt(90)

up()

for x in range(-40, 30):
    for y in range(-40, 30):
        goto(x * m, y * m)
        dot(3, "blue")

update()
exitonclick()