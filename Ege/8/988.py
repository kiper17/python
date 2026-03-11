from itertools import *

k=0
for x in product('аимря',repeat=4):
    s = ''.join(x)
    k+=1
    if s=='ария':
        print(k)
        exit()