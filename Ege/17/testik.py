f = open('17.txt')
a= [int(s) for s in f]

res=[]
for i in range(len(a)-1):
    s = a[i]+a[i+1]
    s1= a[i]*a[i+1]
    if s%2==0 and s1%2!=0:
        res.append(s)

print(len(res),max(res))