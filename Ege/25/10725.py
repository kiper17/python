import re

def f(x):
    D = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            if d%2==0:
                D.add(d)
            if (x//d)%2==0:
                D.add(x//d)
    return D

for x in range(65001, 1000000):
    if re.fullmatch(r'6\d*97\d*5\d', str(x)):
        if len(f(x))>=4:
            print(x, sum(f(x)))