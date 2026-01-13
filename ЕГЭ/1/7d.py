from itertools import *

s1 = '1457 2567 345 435 5123467 625 7125'
s2 = 'АБДВ БЕАД ВАГ ГДВ ДЖГЕАБВ ЕЖДБ ЖДЕ'
s2 = {x[0]:set(x) for x in s2.split()}

for p in permutations("АБВГДЕЖ"):
    s3 = s1
    for x, y in zip("1234567", p):
        s3 = s3.replace(x, y)
    s3 = {x[0]:set(x) for x in s3.split()}
    if s2==s3:
        print(p)