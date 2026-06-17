
k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    p=0
    o=0
    for i in a:
        if i%5!=0:
            p+=1
        if ((i/10) >=1 and (i/10)<10):
            o+=1
    if (p==6 and o!=6) or (p!=6 and o==6):
        k+=1

print(k)