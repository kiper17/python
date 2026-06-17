from math import dist

data=[]
for line in open('task_25447_B.txt'):
    x,y =[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(i,p)<1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

clusters = [cl for cl in clusters if len(cl)>1]
def centroid(cl):
    m=[]
    for p in cl:
        sm = sum(dist(p, p2) for p2 in cl)
        m.append([sm,p])
    return min(m)[1]

def sr(cl, centroid):
    return sum([dist(p, centroid) for p in cl]) / (len(cl)-1)

centroids = [centroid(cl) for cl in clusters]

# A1 = int(abs(min(x for x,y in centroids))*10000)
# A2 = int(abs(min(y for x,y in centroids))*10000)
# print(A1, A2)

B1 = int(abs(sr(clusters[2], centroids[2]))*10000)
B2 = int(abs(sr(clusters[0], centroids[0]))*10000)
print(B1, B2)

#115252 58612
#9106 8973