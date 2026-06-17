from itertools import *

k=0
for x in product('01234567',repeat=5):
    s = ''.join(x)
    if s[0]!='0' and s.count('6')==1:
        s = s.replace('1','3').replace('5','3').replace('7','3')
        if '36' not in s and '63' not in s:
            k+=1
print(k)