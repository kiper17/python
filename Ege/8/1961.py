from itertools import *

k=0
for x in product('елкмр',repeat=4):
    s = ''.join(x)
    k+=1
    if s == 'леее':
        print(k)