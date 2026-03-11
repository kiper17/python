from itertools import *

k=0
b = []
for x in set(permutations('парижанка',r=9)):
    s =''.join(x)
    s = s.replace('и','а')
    if s.count('аа')==1 and 'ааа' not in s:
        k+=1



print(k)