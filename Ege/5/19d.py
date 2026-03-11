for n in range(100,1000):
    d = str(n)
    a = [d[0]+d[1], d[1]+d[2]]
    a = [int(x) for x in a]
    r = max(a)-min(a)
    if r==44:
        print(n,r)

#хз какое решение