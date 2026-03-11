from itertools import *

s1 = '123567 2145 3146 423 5127 6137 7156'
s2 = 'ABDE BADC CBDF DABCEF EADG FCDG GEF'
s2 = {x[0]:set(x) for x in s2.split()}

for p in permutations("ABCDEFG"):
    s3 = s1
    for x, y in zip("1234567",p):
        s3 = s3.replace(x, y)

    s3 = {x[0]:set(x) for x in s3.split()}
    if s2==s3:
        print(p)