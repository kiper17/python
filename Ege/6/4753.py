from turtle import *

tracer(0)
screensize(10,10)
m=30

for i in range(16):
    lt(36)
    fd(4*m)
    lt(36)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#31