from math import dist

data = []
for line in open('task_20130_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p,i)<1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def d(cl):
    m = []
    for p in cl:
        for p2 in cl:
            sm = dist(p, p2)
            m.append([sm,p,p2])
    return max(m)[1:]

dm = []
for cl in clusters: dm.extend(d(cl))

A1 = abs(int(sum(x for x,y in dm)/len(dm)*10000))
A2 = abs(int(sum(y for x,y in dm)/len(dm)*10000))
print(A1, A2)

#16730 48696
#23982 47539