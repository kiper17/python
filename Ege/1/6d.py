from itertools import *

s1 = '12346 216 31678 417 568 61235 734 835'
s2 = 'ABC BACED CADEF DBG FCH GDE HEF EBCGH'
s2 = {x[0]:set(x[1:]) for x in s2.split()}

for p in permutations('ABCDEFGH'):
    s3 = s1
    for x,y in zip('12345678',p):
        s3 = s3.replace(x,y)

    s3 = {x[0]:set(x[1:]) for x in s3.split()}
    if s2==s3:
        print(p)

#чё за мутки нахуй, схуяли не выводит