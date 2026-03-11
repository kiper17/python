from itertools import *

k=0
for x in product('пуля',repeat=6):
    s = ''.join(x)
    if s.count('у')==2:
        k+=1

print(k)