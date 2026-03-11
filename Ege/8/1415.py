from itertools import *

k=0
for x in product('аб123',repeat=8):
    s = ''.join(x)
    if (s.count('а')+s.count('б'))==2:
        k+=1

print(k)