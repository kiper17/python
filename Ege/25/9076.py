from fnmatch import fnmatch 

for x in range(2023, 10**9+1, 2023):
    if sum(map(int, str(x)))<20 and sum(map(int, str(x)))%7==0:
        if fnmatch(str(x),'20*23'):
            print(x,x//2023)