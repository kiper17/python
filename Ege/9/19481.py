

k=0
n=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    a.sort()
    k+=1
    cnt = [a.count(x) for x in a]
    if cnt.count(1) ==4 and (max(a) + min(a))**2 > (a[1]**3 + a[2]**3):
        n+=k

print(n)