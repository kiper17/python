from itertools import *

k=0
for x in permutations('абиколун',r=8):
    s = ''.join(x)
    s = s.replace('а','и').replace('о','и').replace('у','и').replace('к','б').replace('л','б').replace('н','б')
    if 'ии' not in s and 'бб' not in s:
        k+=1

print(k)