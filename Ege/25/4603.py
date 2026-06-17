import re

for x in range(141, 10**8+1, 141):
    if re.fullmatch(r'1234\d*7', str(x)):
        print(x, x//141)