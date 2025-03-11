from itertools import permutations

a = '568 578 567 678 123 134 234 1247'.split()
s = 'АБ БВ ВГ АГ АД БЕ ВИ КГ КД ДЕ ЕИ ИК ДИ'.split()

print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДИЕК'):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
        print(*p)