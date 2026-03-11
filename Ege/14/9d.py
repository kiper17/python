def cc(x):
    s = ''
    while x>0:
        s = str(x%6)+s
        x=x//6
    return s

for i in range(1,100):
    a = cc(36**17 -6**i +71)
    if sum(int(d) for d in a)==61:
        print(i)