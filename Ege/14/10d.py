def cc(x):
    s = ''
    while x>0:
        s = str(x%6)+s
        x=x//6
    return s

a = cc(5 * 216**1156 - 4 * 36**1147 + 6**1153 - 875)
print(a.count("5") - a.count("0"))