from itertools import *

k=0
for x in permutations('игрок',r=5):
    s = ''.join(x)
    if s[0] != 'к' and 'рок' not in s:
        k+=1

print(k)