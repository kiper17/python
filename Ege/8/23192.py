from itertools import *

k=0
for x in product('еиортя',repeat=6):
    s = ''.join(x)
    k+=1
    if k%2!=0 and s[0] not in 'ртя' and s.count('и')>=2:
        print(k,s)