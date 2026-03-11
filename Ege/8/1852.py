from itertools import *

k=0
for x in product('гепард',repeat=5):
    s = ''.join(x)
    if s.count('г')==1 and s[0]!='а' and s[3]!='е':
        k+=1

print(k)