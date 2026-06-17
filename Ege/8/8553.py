from itertools import *

k=0
for x in product('аелмнорь',repeat=6):
    s = ''.join(x)
    k+=1
    if s[0]+s[1]+s[2]+s[3]=='норм':
        print(k)
    if s == 'ненорм':
        print(k,s)

print(137588-154817+1)
    