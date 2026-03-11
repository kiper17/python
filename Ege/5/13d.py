for n in range(1,1500):
    b = bin(n)[2:]
    k1 = 0
    k0 = 0
    for i in range(len(b)):
        if i%2==0:
            if b[i]=='1':
                k1+=1
        else:
            if b[i]=='0':
                k0+=1
    r = k1-k0
    if r==5:
        print(n,r)