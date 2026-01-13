from itertools import *

def f(x,y,z,w):
    return y or (x and w) or (w==z)

for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
    t = [(a1,0,0,a2),(1,1,0,a3),(1,a4,a5,0)]
    if len(t)==len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
                print(p)