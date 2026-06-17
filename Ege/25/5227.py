import re

def f(x):
    D = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            D.add(d)
            D.add(x//d)
    return D

def f1(x):
    D = set()
    for d in range(2, int(x**0.5)+1):
        if x%d==0:
            D.add(d)
            D.add(x//d)
    return D

for x in range(1, 10**7+1):
    if re.fullmatch(r'3\d*52\d', str(x)) and len(f(x))%2!=0:
        print(x, max(f1(x)))