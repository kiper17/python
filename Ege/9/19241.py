
k=0
res=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    cnt = [a.count(x) for x in a]

    k+=1
    np = [x for x in a if a.count(x)==1]
    p = [x for x in a if a.count(x)>1]
    if cnt.count(3)==6 and cnt.count(1)==1:
        if sum(p)/6 < sum(np):
            res=k

print(res)