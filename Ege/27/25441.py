from math import dist

data = []
for line in open('task_25441_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(i, p)<0.25]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def centroid(cl):
    m=[]
    for p in cl:
        sm = sum(dist(p, p2) for p2 in cl)
        m.append([sm,p])
    return min(m)[1]

def ma(cl, centroids):
    return max([dist(p, centroids) for p in cl])

clusters = [cl for cl in clusters if len(cl)>2]
centroids = [centroid(cl) for cl in clusters]

# A1 = int((abs(centroids[0][0]-centroids[1][0]))*10000)
# A2 = int((abs(centroids[0][1]-centroids[1][1]))*10000)
# print(A1, A2)

B1 = int((abs(dist(centroids[1], centroids[0])))*10000)
B2= int((abs(max(ma(clusters[i], centroids[i]) for i in range(3))))*10000)
print(B1, B2)

#18236 93042
#9163 1646