from turtle import *

tracer(0)
screensize(10000,10000)
m=15

lt(90)
lt(255)
for i in range(3):
    lt(30)
    for _ in range(4):
        fd(10*m)
        lt(90)

up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#56