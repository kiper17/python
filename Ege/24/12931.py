from re import *

s = open('24.txt').readline()
r = r'([VWXYZ]|[WXYZ]|[XYZ]|[YZ]|[Z])*[VWXYZ]+([V]|[VW]|[VWX]|[VWXY]|[VWXYZ])*'

print(max([len(x.group()) for x in finditer(r,s)]))