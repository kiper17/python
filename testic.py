
def f(a1,a2,x):
    P = 10<=x<=32
    Q = 18<=x<=45
    A = a2<=x<=a1
    return ((P and (not A))<=(not Q))

res=[]
t = [t for x in [10,18,32,45] for t in [x-0.1,x,x+0.1]]
for a1 in t:
    for a2 in t:
        if a2>a1:
            if all(f(a1,a2,x) for x in t):
                res.append(a2-a1)

print(min(res))