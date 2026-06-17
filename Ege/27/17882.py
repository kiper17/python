from math import dist

data = []
for line in open('task_17882_B.txt'):
    x,y = [float(k) for k in line.replace(',', '.').split()]
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

def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

centroids = [centroid(cl) for cl in clusters]
# A1 = int((centroids[0][0]+centroids[1][0])*5000)
# A2 = int((centroids[0][1]+centroids[1][1])*5000)
# print(A1, A2) 

B1 = int((centroids[0][0]+centroids[1][0]+centroids[2][0])*10000/3)
B2 = int((centroids[0][1]+centroids[1][1]+centroids[2][1])*10000/3)
print(B1, B2)

#10738 30730
#37522 51277