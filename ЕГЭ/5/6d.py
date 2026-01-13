for n in range(1,100):
    b = bin(n)[2:]
    b1 = ''
    for i in range(1,len(b)+1):
        b1 += b[-1 * i]
    r = int(b1,2)
    if r<100:
        print(n,r)