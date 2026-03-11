def cc(x):
    s = ''
    while x>0:
        s = str(x%5)+s
        x=x//5
    return s

for x in range(10000):
    a = 125**200 - 5**x + 74
    b=cc(a)
    if b.count("4")==100:
        print(x)