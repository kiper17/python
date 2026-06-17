from itertools import *

k=0
for x in product('гафний',repeat=4):
    s = ''.join(x)
    if s[0]!= 'й':
        s = s.replace('а','и')
        if s.count('и')>=1:
            k+=1

print(k)