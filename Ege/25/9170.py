import re

def f(x):
    D = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            if re.fullmatch(r'4\d*', str(d)):
                D.add(d)
            if re.fullmatch(r'4\d*', str(x//d)):
                D.add(x//d)
    return D

for x in range(1, 10**6):
    if len(f(x))==24:
        print(x, max(f(x)))