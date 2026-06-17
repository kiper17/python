

for x in range(21):
    c1 = int('8293402',21)+ x*21
    c2 = int('2924007',21) + x*21**2 + x*21
    c3 = int('6756408',21) + x*21
    ch = c1+c2+c3
    if ch%20==0:
        print(x, ch//20)