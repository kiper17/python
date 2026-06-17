from math import dist

data=[]
for line in open('task_18314_A.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if (abs(i[0]-p[0])+abs(i[1]-p[1]))<3]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def centroid(cl):
    m =[]
    for p in cl:
        sm = sum((abs(p1[0]-p[0])+abs(p1[1]-p[1])) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cl) for cl in clusters]

A1 = abs(int(sum(x for x,y in centroids)/len(centroids)*1000))
A2 = abs(int(sum(y for x,y in centroids)/len(centroids)*1000))
print(A1, A2)

#23130 635
#3078 4758