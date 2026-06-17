f = open('17.txt')
a = [int(s) for s in f]

su = sum([x for x in a if x<0])

res=[]
for i in range(len(a)-2):
    sp = [a[i],a[i+1],a[i+2]]
    if max(sp)*min(sp)>su:
        res.append(sum(sp))

print(len(res), max(res), min(res))