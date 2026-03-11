from itertools import *

k=0
for x in permutations('01234567',r=5):
    s = ''.join(x)
    if s.count('1')==0 and s[0]!='0':
        s = s.replace('3','1').replace('0','2').replace('4','2').replace('6','2').replace('5','1').replace('7','1')
        if '11' not in s and '22' not in s:
            k+=1

print(k)