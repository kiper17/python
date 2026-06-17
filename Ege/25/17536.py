
def f(x):
    D = set()
    for d in range(2, int(x**0.5)+1):
        if x%d==0:
            D.add(d)
            D.add(x//d)
    if len(D)==0:
        return 0
    else:
        return max(D)+min(D)

for x in range(800_001,801_000):
    if f(x)%10==4:
        print(x, f(x))