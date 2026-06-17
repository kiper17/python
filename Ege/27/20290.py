from math import dist

data=[]
for line in open('task_20290_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p, i)<0.5]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

clusters = [cl for cl in clusters if len(cl)>1896]

def kr(cl):
    m = []
    for p in cl:
        k = sum([dist(p, p1) for p1 in cl if p!=p1])
        m.append([k,p])
    return max(m)[1]

krai = [kr(cl) for cl in clusters]
A1 = abs(int(sum(x for x,y in krai)*10000/len(krai)))
A2 = abs(int(sum(y for x,y in krai)*10000/len(krai)))
print(A1, A2)

#11575 4282
#4228 16951