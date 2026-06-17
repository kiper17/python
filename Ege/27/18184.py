# from math import dist

# data = []
# for line in open('task_18184_A.txt'):
#     x,y  = [float(k) for k in line.replace(',','.').split()]
#     data.append([x,y])
# print(len(data))
# print()

# #A
# #2
# #1 1 2
# #20 20 3
# ch = [[1, 1], [20, 20]]

# clusters = []
# while data:
#     clusters.append([ch.pop(0)])
#     for p in clusters[-1]:
#         sosedi = [i for i in data if 1<=dist(p, i)<=3]
#         clusters[-1].extend(sosedi)
#         for p2 in sosedi: data.remove(p2)
#     print(len(clusters[-1]))


from math import dist

f = open('task_18184_B.txt')

n = int(f.readline())

blacks = []
for _ in range(n):
    x, y, r = map(float, f.readline().split())
    blacks.append([x, y, r])

stars = []
for line in f:
    x, y = map(float, line.split())
    stars.append([x, y])

ans = []

for x0, y0, r in blacks:
    dists = []

    for x, y in stars:
        d = dist([x0, y0], [x, y])

        if r <= d <= 3 * r:
            dists.append(d - r)

    sr = sum(dists) / len(dists)
    ans.append(int(sr * 1000))

print(max(ans), min(ans))

#3408 2439
#6561 3294