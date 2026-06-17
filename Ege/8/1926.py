from itertools import *

k=0
for x in product('012345',repeat=5):
    s=''.join(x)
    if s[0]!='0':
        s = s.replace('1','3').replace('5','3').replace('0','2').replace('4','2')
        if '33' not in s and '22' not in s:
            k+=1

print(k)