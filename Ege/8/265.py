from itertools import *

k=0
for x in product('агилморт',repeat=4):
    s = ''.join(x)
    k+=1
    if s[2]=='и' and s[3]=='м':
        print(k)