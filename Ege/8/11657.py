from itertools import *

k=0
for x in permutations('01234567',r=6):
    s= ''.join(x)
    if s[0]!='0' and s.count('3')==0:
        s = s.replace('0','2').replace('4','2').replace('6','2')
        if '22' in s:
            k+=1

print(k)