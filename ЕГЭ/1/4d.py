from itertools import *

s1 = '1347 2356 3124567 413 523 6237 7136'
s2 = 'АБГВ БАГЕ ВАГ ГАБВЕДЖ ДГЕЖ ЕБГД ЖГД'
s2 = {x[0]:set(x) for x in s2.split()}

for p in permutations('АБВГДЕЖ'):
    s3 = s1
    for x, y in zip('1234567', p):
        s3 = s3.replace(x, y)
    s3 = {x[0]:set(x) for x in s3.split()}
    if s2==s3:
        print(p)