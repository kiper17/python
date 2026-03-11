for n in range(2,100):
    b = bin(n)[2:]
    s = b[1]
    s1 = b[:-1] + s * 2
    r = int(s1,2)
    if r>58:
        print(n,r)