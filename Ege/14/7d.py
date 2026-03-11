def cc(x):
    s = ''
    d = '0123456789abcdefghijklmnopqrstuvwxy'
    while x>0:
        s = d[x%25]+s
        x=x//25
    return s

a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 *125**5 - 2 * 25**4 - 2024
print(cc(a).count("0"))