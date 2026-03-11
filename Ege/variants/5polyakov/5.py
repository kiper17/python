def cc(x):
    s = ''
    while x>0:
        s = str(x%5)+s
        x=x//5
    return s

for n in range(1,100):
    b = cc(n)
    if b[-1]=='0':
        b = b.replace('4','i').replace('1','4').replace('i','1')
        b = '33' + b
    else:
        b = b + '44'
        b = '3' + b[1:-1] + '2'
    r = int(b,5)
    if r<1922:
        print(n,r)
