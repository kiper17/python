import re

def p(x):
    return x>1 and all(x%d!=0 for d in range(2, int(x**0.5)+1))

for x in range(1, 10**7+1):
    if re.fullmatch(r'3\d1111\d*', str(x)) and p(x):
        print(x, 1)