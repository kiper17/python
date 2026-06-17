from math import *

data=[]
for line in open('task_20217_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters =[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p, i)<1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def cn(cl):
    x = 0
    y = 0
    k = len(cl)
    for p in cl:
        x+=p[0]
        y+=p[1]
    return [x/k, y/k]

centroid = [cn(cl) for cl in clusters]

A1 = abs(int(sum(x for x,y in centroid)*10000/len(centroid)))
A2 = abs(int(sum(y for x,y in centroid)*10000/len(centroid)))
print(A1, A2)

#31190 46669
#35259 61499