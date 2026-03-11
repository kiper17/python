from turtle import *

tracer(0)
screensize(10000,10000)
m=15

for i in range(2):
    fd(24*m)
    rt(90)
    fd(10*m)
    rt(90)

fd(3*m)
lt(90)
fd(13*m)
rt(90)

for i in range(2):
    fd(9*m)
    rt(90)
    fd(32*m)
    rt(90)

up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#120