

k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    a.sort()
    p=0
    p1=[]
    for x in a:
        if x%3==0:
            p+=1
            p1.append(x)
    
    if (max(a)-min(a)) <= sum(p1) and p==3:
        k+=1

print(k)