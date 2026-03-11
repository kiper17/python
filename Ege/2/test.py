# from itertools import *

# def f(x,y,z):
#     return (x<=y)and(y<=z)

# table = [(1,0,0),(1,0,1)]

# for p in permutations('xyz'):
#     if [f(**dict(zip(p, row))) for row in table]==[0,1]:
#         print(p)


# from itertools import *

# def f(x,y,z):
#     return ((not x) and y and z) or ((not x) and (not z))

# table = [(0,0,0),(1,0,0),(1,1,0)]

# for p in permutations('xyz'):
#     if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
#         print(p)


# from itertools import *

# def f(x,y,z,w):
#     return (not y) or x or ((not z) and w)

# table = [(0,0,0,1),(0,0,1,1),(1,0,1,1)]

# for p in permutations('xyzw'):
#     if [f(**dict(zip(p, row))) for row in table]==[0,0,0]:
#         print(p)


# from itertools import *

# def f(a,b,c,d):
#     return (a<=d) and (not(b<=c))

# table = [(1,0,1,0),(1,1,1,0),(0,0,1,0)]

# for p in permutations('abcd'):
#     if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
#         print(p)


# from itertools import *

# def f(x,y,z,w):
#     return ((y<=x)or((not z) and w))==(w==x)

# for a in product([0,1], repeat=3):
#     table = [(a[0],1,0,0),(0,0,0,1),(0,1,a[1],a[2])]
#     if len(table)==len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
#                 print(p)


# from itertools import *

# def f(x,y,w,z):
#     return (x==(not y))<=((x and w)==z)

# for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
#     table = [(1,1,a1,a2),(1,1,a3,1),(a4,1,1,a5)]
#     if len(table)==len(set(table)):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, row))) for row in table]==[0,0,0]:
#                 print(p)


# from itertools import *

# def f(x,y,w,z):
#     return ((x<=z)<=y)or(not w)

# for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):   
#     table = [(1,0,a1,a2),(a3,1,0,a4),(0,a5,a6,a7)]
#     if len(table)==len(set(table)):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, row))) for row in table]==[0,0,0]:
#                 print(p)


# from itertools import *

# def f(x,y,w,z):
#     return (x==y)<=(z==w)

# table = [(0,0,0,1),(1,1,1,0)]
# for p in permutations('xyzw'):
#     if [f(**dict(zip(p,row))) for row in table]==[0,0]:
#         print(p)


from itertools import *

def f(x,y,w,z):
    return (x and (y<=z)) or w
    
d = set()
for a1,a2,a3,a4,a5,a6 in product([0,1], repeat=6):   
    table = [(1,0,a1,1),(a2,0,1,a3),(a4,0,a5,a6)]
    if len(table)==len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table]==[0,0,0]:
                d.add(p)

print(len(d))
