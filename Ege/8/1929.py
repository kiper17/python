from itertools import *

k=0
for x in permutations('дейкстра',r=6):
    s = ''.join(x)
    if s.count('й')==1 and (('йд' in s) or ('йк' in s) or ('йс' in s) or ('йт' in s) or ('йр' in s)):
        k+=1

print(k)