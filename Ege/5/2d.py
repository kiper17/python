for n in range(1,100):
    b = bin(n)[2:]
    if int(b)%2==0:
        b = b + "01"
    else:
        b = b + "10"
    r = int(b,2)
    if r>81:
        print(n,r)