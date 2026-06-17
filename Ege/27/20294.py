from math import dist

data = []
for line in open('task_20294_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p, i)<0.35]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def isolat(cl):
    m = []
    for p in cl:
        sm = len([p2 for p2 in cl if dist(p, p2)<1])
        m.append([sm, p])
    return min(m)[1]

isolated = [isolat(cl) for cl in clusters]
A1 = abs(int(sum(x for x,y in isolated)*100000/len(isolated)))
A2 = abs(int(sum(y for x,y in isolated)*100000/len(isolated)))
print(A1,A2)

#135491 131265
#232818 15126