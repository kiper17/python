from itertools import *

k=0
for x in product('012345',repeat=7):
    s=''.join(x)
    if s[0]!='0' and s.count('2')==1:
        s = s.replace('0','4')
        if '42' not in s and '24' not in s:
            k+=1

print(k)