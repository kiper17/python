# from itertools import *

# a = "248 157 456 136 23 34 28 17"
# s = "FBE AHE FGH GH AB AC CD CDB"

# d = {frozenset(x) for x in s.split()}

# for p in permutations("ABCDEFGH"):
#     a1 = a
#     for x, y in zip('12345678',p):
#         a1 = a1.replace(x, y)
    
#     a1 = {frozenset(x) for x in a1.split()}
#     if a1 == d:
#         print(p)


# from itertools import *

# s1 = '256 134 267 27 16 34 135'
# s2 = "FB AFD EG BEG FDC ABE CD"

# s2 = {frozenset(x) for x in s2.split()}

# for p in permutations("ABCDEFG"):
#     s3 = s1
#     for x, y in zip('1234567', p):
#         s3 = s3.replace(x,y)
#     s3 = {frozenset(x) for x in s3.split()}
#     if s2==s3:
#         print(p)


# from itertools import *

# s1 = '37 57 147 37 26 57 12346'
# s2 = "CDG DF AD ACGBE DF BE AD"

# s2 = {frozenset(x) for x in s2.split()}

# for p in permutations("ABCDEFG"):
#     s3 = s1
#     for x, y in zip('1234567', p):
#         s3 = s3.replace(x,y)
#     s3 = {frozenset(x) for x in s3.split()}
#     if s2==s3:
#         print(p)


# from itertools import *

# s1 = "4578 367 26 15 148 238 128 1567"
# s2 = "БИ АИЖВ БЖГ ВЕД ГЕ ЖГД ИБВЕ АБЖ"

# s2 = {frozenset(x) for x in s2.split()}

# for p in permutations("АБВГДЕЖИ"):
#     s3 = s1
#     for x,y in zip("12345678", p):
#         s3 = s3.replace(x,y)
#     s3 = {frozenset(x) for x in s3.split()}
#     if s2==s3:
#         print(p)


# from itertools import *

# s1 = "468 456 578 12 2368 125 38 1357"
# s2 = "ЕГ ГДВ БИ АЕБЖ БЖИ АГЖ ЕГДИ ЖДВ"
# s2 = {frozenset(x) for x in s2.split()}

# for p in permutations("АБВГДЕЖИ"):
#     s3 = s1
#     for x,y in zip("12345678", p):
#         s3 = s3.replace(x,y)
#     s3 = {frozenset(x) for x in s3.split()}
#     if s2==s3:
#         print(p)


# from itertools import *

# s1 = '158 234 328 4268 517 6478 7568 813467'
# s2 = 'АВЕ БГЖ ВАД ГДБ ДВЕЗЖГ ЕАДЗ ЖЗДБ ЗЕДЖ'
# s2 = {x[0]:frozenset(x[1:]) for x in s2.split()}

# for p in permutations("АБВГДЕЖЗ"):
#     s3 = s1
#     for x,y in zip("12345678", p):
#         s3 = s3.replace(x,y)

#     s3 = {x[0]:frozenset(x[1:]) for x in s3.split()}
#     if s3==s2:
#         print(p)


# from itertools import *

# s1 = "1457 2358 32458 41367 5123 6478 7146 8236"
# s2 = 'АБГЕ БАДВ ВБДИ ГАЕЖД ДГБВИ ЕАГЖ ЖЕГИ ИЖДВ'
# s2 = {x[0]:frozenset(x[1:]) for x in s2.split()}

# for p in permutations("АБВГДЕЖЗИ"):
#     s3 = s1
#     for x,y in zip("12345678", p):
#         s3 = s3.replace(x,y)

#     s3 = {x[0]:frozenset(x[1:]) for x in s3.split()}
#     if s2==s3:
#         print(p)


# from itertools import *

# s1 = '127 2178 3457 437 537 678 71234568 8267'
# s2 = 'ABCDEFGH BAC CBAD DAC EAF FEAG GFAH HAG'
# s2 = {x[0]:frozenset(x[1:]) for x in s2.split()}

# for p in permutations("ABCDEFGH"):
#     s3 = s1
#     for x,y in zip("12345678", p):
#         s3 = s3.replace(x,y)

#     s3 = {x[0]:frozenset(x[1:]) for x in s3.split()}
#     if s2==s3:
#         print(p)


# from itertools import *

# s1 = '12467 21357 325 4156 52346 6145 712'
# s2 = 'АБВГ БАВЕЖ ВАБГ ГАВЕД ДГЕ ЕЖБГД ЖБЕ'
# s2 = {x[0]:frozenset(x[1:]) for x in s2.split()}

# for p in permutations("АБВГДЕЖ"):
#     s3 = s1
#     for x,y in zip("1234567", p):
#         s3 = s3.replace(x,y)

#     s3 = {x[0]:frozenset(x[1:]) for x in s3.split()}
#     if s2==s3:
#         print(p)


from itertools import *

s1 = '147 257 345 4136 5236 6457 7126'
s2 = 'AGE BFDC CBGE DBE EACD GFCA FBG'
s2 = {x[0]:frozenset(x[1:]) for x in s2.split()}

for p in permutations("ABCDEFG"):
    s3 = s1
    for x,y in zip("1234567", p):
        s3 = s3.replace(x,y)

    s3 = {x[0]:frozenset(x[1:]) for x in s3.split()}
    if s2==s3:
        print(p)