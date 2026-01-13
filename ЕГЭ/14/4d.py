def cc(x):
    s = ''
    while x>0:
        s = str(x%7)+s
        x=x//7
    return s

a = cc(51*7**12 - 7**3 - 22)
k = 0
for i in range(len(a)):
    k+=int(a[i])
print(k)