from math import dist

data=[]
for line in open('task_20291_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p,i)<0.4]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def d(cluster):
    sm=0
    for p in cluster:
        for p2 in cluster:
            sm = max(sm, dist(p, p2))
    return sm

dm = [d(cl) for cl in clusters]
A1 = int(min(dm)*100000)
A2 = int(sum(dm)/7*100000)
print(A1, A2)

#208364 305606
#544492 600793