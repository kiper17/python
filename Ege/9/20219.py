

k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    p=0
    l=0
    for x in a:
        if (x/10)>=10 and (x/10)<100:
            p+=1
        if x %5 !=0:
            l+=1
    if p>=3 and l==6:
        k+=1

print(k)