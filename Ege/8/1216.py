from itertools import *

k=0
for x in product('01234',repeat=6):
    s = ''.join(x)
    if s[0] not in '01' and s[5] != '3' and s[5] != '4':
        k+=1

print(k)