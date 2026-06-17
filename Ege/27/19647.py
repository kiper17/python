from math import dist

data = []
for line in open('task_19647_B.txt'):
    x,y = [float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))
print()

#0,4
#0,1

# clusters = []
# while data:
#     clusters.append([data.pop(0)])
#     for p in clusters[-1]:
#         sosedi = [i for i in data if dist(p, i)<0.7]
#         clusters[-1].extend(sosedi)
#         for p2 in sosedi: data.remove(p2)
#     print(len(clusters[-1]))

print()

def centroid(cl):
    m = []
    for p in data:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

# centroids = [centroid(cl) for cl in clusters]
# print(centroids)

a = [[9.3076, 21.1009], [13.0057, 15.9721], [12.2501, 24.1383]]
print(*[10000*x for x in centroid(a)])

#23392 26712
#101947 210484