from turtle import *

tracer(0)
screensize(1000,1000)
m=20

for i in range(3):
    fd(7*m)
    rt(90)

fd(8*m)

for i in range(3):
    lt(90)
    fd(5*m)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'blue')

update()
exitonclick()

#12+8-5+16+12=43