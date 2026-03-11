from itertools import *

k=0
for x in permutations('0123456789abc',r=7):
    s = ''.join(x)
    if s[0]!='0':
        s = s.replace('3','1').replace('5','1').replace('7','1').replace('9','1')
        if '1b' not in s and 'b1' not in s:
            k+=1

print(k)