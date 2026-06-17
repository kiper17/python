from re import *

s = open('24.txt').readline()
r = r'((NPO)|(PNO))+'

print(max([len(x.group())//3 for x in finditer(r,s)]))