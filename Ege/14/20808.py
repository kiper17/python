
m=[]
for x in range(1,2031):
    a= 7**170 + 7**100 - x
    k0=0
    while a>0:
        if a%7==0:
            k0+=1
        a=a//7
    m.append(k0)
    if k0==73:
        print(x)

print(max(m))