for n in range(1,1000):
    k1 = k2 = 0
    d = str(n)
    d = [int(c) for c in d]
    k1 = sum(c for c in d if c%2==0)
    for i in range(len(d)):
        if (i+1)%2==0: k2+=d[i]
    r = abs(k1-k2)
    if r==9:
        print(n,r)