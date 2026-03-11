k=0
for n in range(1,10000):
    r = n
    if r%3==0:
        r =r//3
    else:
        r=r-1
    if r%5==0:
        r=r//5
    else:
        r=r-1
    if r%11==0:
        r=r//11
    else:
        r=r-1
    if r==8:
        k+=1
        print(n,r)
