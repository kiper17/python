def cc(x):
    s = ''
    while x>0:
        s = str(x%4)+s
        x=x//4
    return s

a = 3 * 16**8 - 4**5 + 3
b = cc(a)
print(b.count("3"))