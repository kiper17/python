from turtle import *

tracer(0)
screensize(1000,1000)
m=20

for i in range(15):
    fd(7*m)
    rt(30)
    fd(8*m)
    rt(150)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#28