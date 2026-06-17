

k=0

for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    cnt = [a.count(x) for x in a]
    np = [x for x in a if a.count(x)==1]
    p3 = [x for x in a if a.count(x)==3]
    if cnt.count(3)==3 and cnt.count(1)==3:
        if sum(p3)**2 > sum(np)**2:
            k+=1

print(k)