import re

def cc(x):
    k = []
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            k.append(d)
            if d * d != x:
                k.append(x // d)
    return k

for x in range(53, 10**7+1, 53):
    if re.fullmatch(r'\d*2\d2\d*', str(x)):
        if str(x)==str(x)[::-1]:
            if len(cc(x))>30:
                print(x,sum(cc(x)))