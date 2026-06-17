from math import dist

data = []
for line in open('task_23766_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(i,p) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

clusters = [cl for cl in clusters if len(cl)>10]

def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

def max_dist(cl, centroid):
    return max([dist(p, centroid) for p in cl])

centroids = [centroid(cl) for cl in clusters]
# A1 = int((min(centroids[0][0], centroids[1][0]))*10000)
# A2 = int((min(centroids[0][1],centroids[1][1]))*10000)
# print(A1, A2)

B1 = int(dist(centroids[0], centroids[1])*10000)
B2 = int((max(max_dist(clusters[i], centroids[i]) for i in range(len(clusters))))*10000)

print(B1, B2)

#38471 61225
#95081 25299