from itertools import *

k=0
k1=0
for x in product('агдейсэ',repeat=6):
    s=''.join(x)
    k+=1
    if 'егэ' in s:
        k1+=k

print(k1)