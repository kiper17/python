

k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    cnt = [a.count(x) for x in a]
    ch = [x for x in a if x%2==0]
    nch = [x for x in a if x%2!=0]
    p=0
    if (cnt.count(2)==2 and cnt.count(1)==4):
        p+=1
    if len(ch) !=0 and len(nch)!=0:
        if ((sum(ch)/len(ch) - sum(nch)/len(nch)) > 50 or (sum(ch)/len(ch) - sum(nch)/len(nch)) < -50):
            p+=1
    if len(ch)==0:
        if sum(nch)/len(nch) > 50 or sum(nch)/len(nch) < -50:
            p+=1
    if len(nch)==0:
        if (sum(ch)/len(ch)) > 50 or (sum(ch)/len(ch)) < -50:
            p+=1

    if p==1:
        k+=1

print(k)
