for line in open('9.txt'):
    a = [int(x) for x in line.split()]
    
    # проверка убывания
    if a[0] > a[1] > a[2] > a[3] > a[4] > a[5] > a[6]:
        
        mn = min(a)
        mx = max(a)
        
        b = a.copy()
        b.remove(mn)
        b.remove(mx)
        
        if (mn + mx) / 2 > sum(b) / len(b):
            print(sum(a))
            break
