count = 0

for line in open('9.txt'):
    a = [int(x) for x in line.split()]
    a.sort()
    if a[1]-a[0]==a[2]-a[1]==a[3]-a[2]==a[4]-a[3]==a[5]-a[4] and any(x % 10 == 3 for x in a):
        count+=1

print(count)