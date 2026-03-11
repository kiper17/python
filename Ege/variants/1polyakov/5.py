def cc(x):
    s = ''
    while x>0:
        s = str(x%3)+s
        x = x//3
    return s
a = []
for n in range(1,100):
    b = cc(n)
    if n%3==0:
        b = b + b[-2:]
    else:
        b = b + cc(((n%3)-1)*3)
    r = int(b,3)
    a.append(r)

print(sorted(a))