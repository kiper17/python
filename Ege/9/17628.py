

k=0
for line in open('Ege\9\9.txt'):
    a = [int(x) for x in line.split()]
    if max(a) + min(a) <= sum(a) - max(a) - min(a):
        k+=1

print(k)