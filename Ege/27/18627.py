from math import dist

data = []
for line in open('task_18627_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(i, p)<1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p2) for p2 in cl)
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cl) for cl in clusters]

# A1 = int((sum(x for x,y in centroids))*50000)
# A2 = int((sum(y for x,y in centroids))*50000)
# print(A1, A2)

B1 = int((sum(x for x,y in centroids))*100000/3)
B2 = int((sum(y for x,y in centroids))*100000/3)
print(B1, B2)

#752263 548854
#767186 281688