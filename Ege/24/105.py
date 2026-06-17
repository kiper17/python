from re import *

s = open('24.txt').readline()
r = r'[F]*|[A]*|[I]*|[L]*'

print(max([len(x.group()) for x in finditer(r,s)]))