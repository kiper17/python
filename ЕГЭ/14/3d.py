def cc(x):
    s = ''
    while x>0:
        s = str(x%3)+s
        x=x//3
    return s

a = 2 * 27**7 +3**10 -9
b = cc(a)
print(b.count("0"))