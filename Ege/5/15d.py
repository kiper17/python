for n in range(100,1000):
    d = [int(c) for c in str(n)]
    a = d[0]*d[1]
    b = d[1]*d[2]
    if a>b:
        r = int(str(a)+str(b))
    else:
        r = int(str(b)+str(a))
    if r==240:
        print(n)