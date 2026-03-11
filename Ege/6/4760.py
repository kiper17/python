from turtle import *

tracer(0)
screensize(1000,1000)
m=20

for i in range(14):
    for _ in range(3):
        fd(3*m)
        rt(90)
    lt(180)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#28