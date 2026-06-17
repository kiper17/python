from itertools import *

k=0
for x in permutations('0123456789abcdefg',r=6):
    s = ''.join(x)
    if s[0]!='0':
        s = s.replace('3','1').replace('5','1').replace('7','1').replace('9','1').replace('b','1').replace('d','1').replace('f','1')
        s = s.replace('0','2').replace('4','2').replace('6','2').replace('8','2').replace('a','2').replace('c','2').replace('e','2').replace('g','2')
        if '111' not in s and '222' not in s:
            k+=1
print(k)