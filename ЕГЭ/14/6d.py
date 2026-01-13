def cc(x):
    s = ''
    d = "0123456789abcde"
    while x>0:
        s = d[x%15] + s
        x=x//15
    return s

a = cc(11*15**65 +18*15**38 -14*15**17 +19*15**11 + 18338)
print(set(a))