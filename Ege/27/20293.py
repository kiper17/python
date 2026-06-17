from math import dist

data=[]
for line in open('task_20293_A.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p,i)<0.35]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def tn(cl):
    m=[]
    for p in cl:
        sm = len([p2 for p2 in cl if dist(p,p2)<1])
        m.append([sm,p])
    return max(m)[1]

tocka = [tn(cl) for cl in clusters]
A1 = abs(int(sum(x for x,y in tocka)*100000/len(tocka)))
A2 = abs(int(sum(y for x,y in tocka)*100000/len(tocka)))
print(A1, A2)

#171553 32527
#157853 13516