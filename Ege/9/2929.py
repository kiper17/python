

k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    a.sort()
    if (max(a)+min(a))/2 <= a[1]:
        k+=1

print(k)