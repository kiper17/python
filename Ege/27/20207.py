from math import dist

data=[]
for line in open('task_20207_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
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

def medianx(cluster):
    for p in cluster:
        count=0
        for p2 in cluster:
            if p2[0]>p[0]:
                count+=1
        if count == len(cluster)//2:
            return p[0]

def mediany(cluster):
    for p in cluster:
        count=0
        for p2 in cluster:
            if p2[1]>p[1]:
                count+=1
        if count == len(cluster)//2:
            return p[1]

mx = [medianx(cluster) for cluster in clusters]
my = [mediany(cluster) for cluster in clusters]
A1 = abs(int(sum(mx)/len(mx)*10000))
A2 = abs(int(sum(my)/len(my)*10000))
print(A1, A2)



#40893 9686
#30438 41916