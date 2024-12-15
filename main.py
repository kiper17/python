# from itertools import product, permutations

# def f(x, y, w, z):
#     # ((w → y) → x) ˅ ¬z
#     return (not(not(w) or y) or x) or not(z)

# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
#     t = (
#         (x1, x2, 1, x3, 0),
#         (x4, 0, x5, x6, 0),
#         (x7, 1, 0, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations("xywz", r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in t):
#                 print(*p)

# def f(x, A):
#     return ((x % 7 != 0) and (x % 13 == 0)) <= ( x > A - 40)

# print(max(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, A):
#     return (x % A == 0) or ((40<=x<=50) <= (x % 12 != 0))

# print(max(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, A):
#     return (x&57 == 0) or ((x&23 == 0) <= (x&A != 0))

# print(min(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, y, A):
#     return (x- y >= 39) or (y <= x) or (y >= A - 20)

# print(max(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     M = 32 <= x <= 68
#     N = 54 <= x <= 76
#     A = 0
#     f = (not (M or N)) == (not A)
#     if f != 1:
#         print(x)

# def f(x, y, A):
#     return (x <= 19) or (y < 2 * x + A - 50) or (y > 17)

# print(min(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 15 <= x <= 40
#     Q = 21 <= x <= 63
#     A = 0
#     f = P <= ((Q and (not A)) <= (not P))
#     if f != 1:
#         print(x)

# def f(x, y, A):
#     return (x + y <= 24) or (y <= x - 2) or (y >= A)

# print(max(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# def f(x, y, A):
#     return (x + y <= 30) or (y <= x + 2) or (y >= A)

# print(max(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# def f(x, A):
#     return (x % A == 0) or ((70 <= x <= 90) <= (not x % 22 == 0))

# print(max(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 10

# rt(45)
# for i in range(19):
#     rt(45)
#     fd(203 * m)
#     rt(45)
# up()
# bk(40 * m)
# rt(45)
# down()
# for i in range(5):
#     fd(20 * m)
#     lt(90)

# for x in range(-60, 60):
#     for y in range(-60, 60):
#         goto(x * m, y * m)
#         dot(2, 'red')


# update()
# exitonclick()

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 15

# for i in range(5):
#     fd(15 * m)
#     lt(90)
#     fd(25 * m)
#     lt(90)
# up()
# fd(4 * m)
# lt(90)
# fd(12 * m)
# lt(90)
# down()
# for i in range(6):
#     fd(38 * m)
#     rt(90)
#     fd(22 * m)
#     rt(90)

# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, "red")

# update()
# exitonclick()

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 10

# for i in range(9):
#     fd(50 * m)
#     rt(90)
#     fd(35 * m)
#     rt(90)
# up()
# fd(5 * m)
# rt(90)
# fd(10 * m)
# rt(90)
# down()
# for i in range(4):
#     fd(35 * m)
#     rt(90)
#     fd(17 * m)
#     rt(90)

# up()
# for x in range(-20, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(3, 'red')

# update()
# exitonclick()

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 15

# for i in range(9):
#     fd(22 * m)
#     rt(90)
#     fd(6 * m)
#     rt(90)
# up()
# fd(1 * m)
# rt(90)
# fd(5 * m)
# lt(90)
# down()
# for i in range(9):
#     fd(53 * m)
#     rt(90)
#     fd(75 * m)
#     rt(90)

# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, 'red')

# update()
# exitonclick()

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 15

# for i in range(2):
#     fd(11 * m)
#     rt(90)
#     fd(17 * m)
#     rt(90)
# up()
# fd(7 * m)
# lt(90)
# bk(1 * m)
# rt(90)
# down()
# for i in range(2):
#     fd(15 * m)
#     rt(90)
#     fd(7 * m)
#     rt(90)

# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, 'red')

# update()
# exitonclick()

# 

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 15

# for i in range(3):
#     fd(7 * m)
#     rt(90)
#     fd(12 * m)
#     rt(90)
# up()
# fd(4 * m)
# rt(90)
# fd(6 * m)
# lt(90)
# down()
# for i in range(4):
#     fd(83 * m)
#     rt(90)
#     fd(77 * m)
#     rt(90)

# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x * m, y * m)
#         dot(3, 'red')

# update()
# exitonclick()

# def f(x, y, A):
#     return ( x ** 2 + y ** 2 > 1024 - x ) or (y < -2 * x + A)

# print(min(A for A in range(0, 200) if all(f(x, y, A) == 1 for x in range(0, 2000) for y in range(0, 2000))))

# def f(x, A):
#     return ( A + x > 700 - A) and ((A % 100 + 100 % x) > 50)

# print(min(A for A in range(1, 2000) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, A):
#     return (not ( x % 263 == 0) <= ( x % A == 0)) and ( x % 71 == 0)

# print(max(A for A in range(1, 50000) if all(f(x, A) == 0 for x in range(1, 200000))))

# from turtle import *

# tracer(0)
# screensize(10000, 10000)
# m = 20

# fd(167 * m)
# rt(180)
# fd(51 * m)
# rt(180)
# fd(161 * m)

# for x in range(0, 100):
#     for y in range(-1, 1):
#         goto(x * m, y * m)
#         dot(3, 'red')

# update()
# exitonclick()

count = 0
for line in open('9.txt'):
    a = [int(x) for x in line.split()]
    p1 = [x for x in a if a.count(x) >= 2]
    np = [x for x in a if a.count(x) == 1]
    if len(p1) >= 2:
        if sum(np) % 2 == 0:
            count += 1

print(count)

