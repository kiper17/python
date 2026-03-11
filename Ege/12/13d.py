command = {
    (' ',0): (' ',1,1),
    (' ',1): (' ',2,1),
    ('2',1): ('3',1,1),
    ('3',1): ('8',1,1),
    ('8',1): ('2',1,1),
}

def mt(s):
    s = list(' '+s+' ')
    q = 0
    i = 0
    while True:
        cmd = command[(s[i],q)]
        s[i]=cmd[0]
        if cmd[1]==2: break
        i+=cmd[1]
        q=cmd[2]
    return ''.join(s)

print(sum(map(int, mt('2'*764 + '3'*122 + '8'*114).strip())))