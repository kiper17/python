from math import dist

data=[]
for line in open('task_20295_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p, i)<0.4]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def pl(cl):
    m=[]
    for p in cl:
        k=len([p2 for p2 in cl if dist(p, p2)<1])
        m.append(k)
    return sum(m)/len(m)

p = [pl(cl) for cl in clusters]
A1 = abs(int(min(p)*100000))
A2 = abs(int(sum(p)/len(p)*100000))
print(A1, A2)

#5158000 9476083
#7604400 18899514