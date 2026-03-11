from itertools import *

k=0
for x in product('агдилнря',repeat=6):
    s = ''.join(x)
    k+=1
    if s[0]!='я' and s.count('д')==3 and k%2==0:
        print(k,s)