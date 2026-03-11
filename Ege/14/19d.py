def cc(x):
    s = ''
    while x>0:
        s = str(x%5)+s
        x=x//5
    return s

def cc1(x):
    s = ''
    d = '0123456789abcdef'
    while x>0:
        s = d[x%16]+s
        x=x//16
    return s

k=0
for n in range(1,1000):
    if len(cc(n))<=4 and len(bin(n)[2:])>=5 and cc1(n)[-1]=="c":
        k+=1

print(k)