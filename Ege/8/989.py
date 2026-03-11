from itertools import *

k=0
for x in product('аимря',repeat=4):
    k+=1
    s = ''.join(x)
    if k==211:
        print(s)