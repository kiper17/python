

k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    a.sort()
    if max(a)+min(a)<a[1]+a[2]:
        k+=1

print(k)