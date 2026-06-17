from itertools import *

k=0
for x in set(permutations('анастасия',r=9)):
    s=''.join(x)
    s = s.replace('а','я').replace('и','я').replace('н','с').replace('т','с')
    if not ('яяя' in s and 'ссс' in s):
        k+=1

print(k)