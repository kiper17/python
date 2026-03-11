def cc(x):
    s = ''
    while x>0:
        s = str(x%3)+s
        x=x//3
    return s

for x in range(20,30):
    print(x,cc(x))