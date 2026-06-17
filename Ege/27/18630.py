from math import dist

data=[]
for line in open('task_18630_B.txt'):
    x, y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p, i)<1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

clusters = [cl for cl in clusters if len(cl)>10]
def centroid(cl):
    m = []
    for p in cl:
        sm = sum([dist(p, p2) for p2 in cl])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cl) for cl in clusters]

A1 = abs(int(sum(x for x,y in centroids)*100000/len(centroids)))
A2 = abs(int(sum(y for x,y in centroids)*100000/len(centroids)))
print(A1,A2)

#559397 625605
#923413 613488