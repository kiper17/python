f = open('17.txt')
a= [int(s) for s in f]

su35 = sum(sum(map(int, str(x))) for x in a if x % 35 == 0)

res = []
for i in range(len(a)-1):
    s = a[i]+a[i+1]
    if (a[i]>su35 and (not a[i+1]>su35) and hex(a[i+1])[-2:]=='ef') or (a[i+1]>su35 and (not a[i]>su35) and hex(a[i])[-2:]=='ef'):
        res.append(s)

print(len(res),min(res))