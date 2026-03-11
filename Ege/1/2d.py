from itertools import *

s1 = '156 247 346 4236 516 613457 726'
s2 = 'АБВ БАВ ВАБДКГ ГВК ДВЕ ЕДК КЕГВ'
s2 = {x[0]:set(x) for x in s2.split()}

for p in permutations('АБВГДЕК'):
    s3 = s1
    for x,y in zip('1234567', p):
        s3 = s3.replace(x,y)

    s3 = {x[0]:set(x) for x in s3.split()}
    if s2==s3:
        print(p)