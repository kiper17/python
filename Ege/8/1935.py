from itertools import *

k=0
for x in permutations('вайфу',r=4):
    s = ''.join(x)
    if s[0] != 'й' and 'вф' not in s and 'фв' not in s:
        k+=1

print(k)