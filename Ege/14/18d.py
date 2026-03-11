def cc6(x):
    s=''
    while x>0:
        s=str(x%6)+s
        x=x//6
    return s

def cc5(x):
    s=''
    while x>0:
        s=str(x%5)+s
        x=x//5
    return s

def cc11(x):
    s=''
    d = "0123456789a"
    while x>0:
        s=d[x%11]+s
        x=x//11
    return s

for n in range(1,100):
    if (len(cc6(n))==2 and (len(cc5(n))==3)):
        print(n,cc11(n))