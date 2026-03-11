def cc(x):
    s = ''
    d = '0123456789ab'
    while x>0:
        s = d[x%12]+s
        x=x//12
    return s

a = cc(6*144**26 + 11*12**75 -48)
print(a.count("b"))