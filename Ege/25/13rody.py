
def p(x):
    return x>1 and all(x%d!=0 for d in range(2, int(x**0.5)+1))

def f(x):
    D = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            if p(d):
                D.add(d)
            if p(x//d):
                D.add(x//d)
    if len(D) == 0:
        return 0
    else: return max(D) + min(D)

for x in range(1_101_001, 1_102_000):
    if f(x)>13000 and str(f(x))[-2:]=='26':
        print(x, f(x))
