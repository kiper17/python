import re

for x in range(1923, 10**8+1, 1923):
    if re.fullmatch('1\d*2\d\d76',str(x)):
        print(x,x//1923)