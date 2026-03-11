for n in range(1,100):
    a = (1*(n**2) + 3*n +2) + int("13", 8)
    b = 1*((n+1)**2) + 2*(n+1) + 4
    if a==b:
        print(n)