from turtle import *

tracer(0)
screensize(10000,10000)
m=20

for i in range(8):
    for _ in range(4):
        fd(5*m)
        rt(30)
        fd(6*m)
        rt(150)
    rt(60)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#90