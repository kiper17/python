k = 0
for n in range(1,100):
    b = bin(n)[2:]
    b = b + str(sum(map(int,b))%2)
    b = b + str(sum(map(int,b))%2)
    r = int(b,2)
    if r<80:
        k +=1
print(k)