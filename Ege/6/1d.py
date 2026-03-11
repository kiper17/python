from turtle import *

tracer(0)
screensize(100000,100000)
m = 10
lt(90)

for i in range(100):
    fd(10*m)
    rt(8)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()