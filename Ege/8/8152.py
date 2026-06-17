from itertools import *

k=0
for x in product('иклнор',repeat=4):
    s = ''.join(x)
    k+=1
    if s == 'кино':
        print(k)