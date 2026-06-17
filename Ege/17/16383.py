f = open('17.txt')
a = [int(s) for s in f]

max23 = max([x for x in a if abs(x)%100==21 and 10000<=abs(x)<100000])

res=[]
for i in range(len(a)-1):
    if (abs(a[i]) % 100 == 21 and 10000 <= abs(a[i]) < 100000) != (abs(a[i+1]) % 100 == 21 and 10000 <= abs(a[i+1]) < 100000):
        s = a[i]**2 + a[i+1]**2
        if s>=max23**2:
            res.append(a[i]+a[i+1])


print(len(res), max(res))