from itertools import *

def f(x,y,z):
    return (z==y)==((not y)or(not x))

for a1,a2,a3 in product([0,1], repeat=3):
    t = [(0,0,a1),(a2,a3,0),(1,0,1)]
    for p in permutations('xyz'):
        if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
            print(p)