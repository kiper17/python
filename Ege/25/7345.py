import re

k=[]
k1=[]
for x in range(4546, 10**10+1, 4546):
    if re.fullmatch(r'8\d*80\d*06', str(x)):
        k.append(x)
        k1.append(x//4546)

print(k[0],k1[0])
print(k[60],k1[60])
print(k[120],k1[120])
print(k[180],k1[180])
print(k[240],k1[240])