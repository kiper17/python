
def p(x):
    return x>1 and all(x%d!=0 for d in range(2, int(x**0.5)+1))

def f(x):
    D = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            if d%2==0:
                D.add(d)
            if (x//d)%2==0:
                D.add(x/d)
    return D

def f1(x):
    D = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            if p(d):
                D.add(d)
            if p(x//d):
                D.add(x/d)
    return D

for x in range(100000000, 100001000):
    P = f1(x)
    E = f(x)
    M = abs(sum(P)-sum(E))
    if len(P)==len(E):
        print(x,M)