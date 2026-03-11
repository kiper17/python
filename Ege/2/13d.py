from itertools import *

def f(x,y,z,w):
    return ((w<=y)or(not(y<=z)))and(not x) and (not(x==z))

for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    t = [(0,a1,1,a2),(1,a3,a4,1),(0,a5,1,1)]
    if len(t)==len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
                print(p)