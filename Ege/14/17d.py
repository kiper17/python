for x in range(3,10):
    b = 68
    s = ''
    while b>0:
        s=str(b%x)+s
        b=b//x
    print(x,s)
