from turtle import * # импорт модуля черепахи

tracer(0) # для вырисовки в 1 момент
screensize(10000, 10000) # размер экрана
m = 15 # масштаб

# внизу что делает черепаха
for i in range(2):
    fd(24 * m)
    rt(90)
    fd(10 * m)
    rt(90)
fd(3 * m)
lt(90)
fd(13 * m)
rt(90)
for i in range(2):
    fd(9 * m)
    rt(90)
    fd(32 * m)
    rt(90)

# разметка страницы
up()
for x in range(-40, 30):
    for y in range(-40, 30):
        goto(x * m, y * m)
        dot(3, "blue")

update() # для обновления вырисовки
exitonclick() # выход при клике