from math import dist

data=[]
for line in open('task_20292_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [i for i in data if dist(p,i)<0.35]
        clusters[-1].extend(sosedi)
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def sr(cl):
    sm = 0
    k = 0
    for i in range(len(cl)):
        for j in range(i+1, len(cl)):
            sm+=(dist(cl[i], cl[j]))
            k+=1
    return sm/k

ser = [sr(cl) for cl in clusters]
print(ser)

A1 = int(abs(min(ser))*100000)
A2 = int(abs(max(ser))*100000)
print(A1, A2)

#79724 158994
#205908 237869