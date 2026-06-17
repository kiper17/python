

k=[]
sum1=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    cnt = [a.count(x) for x in a]
    np = [x for x in a if a.count(x)==1]
    p = [x for x in a if a.count(x)>1]
    if cnt.count(3)==3 and cnt.count(1)==3:
        if p[1] < min(np)*2:
            k+=a

print(sum(k)/len(k))