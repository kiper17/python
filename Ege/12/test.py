# command = {
#     (' ',0): (' ',1,1),
#     (' ',1): (' ',2,1),
#     (' ',2): (' ',2,2),
#     (' ',3): (' ',2,3),
#     ('0',1): ('0',1,2),
#     ('0',2): ('1',1,3),
#     ('0',3): ('0',1,2),
#     ('1',1): ('1',1,2),
#     ('1',2): ('0',1,3),
#     ('1',3): ('1',1,1)
# }

# def mt(s):
#     s = list(' '+s+' ')
#     q = 0
#     i = 0
#     while True:
#         cmd = command[(s[i],q)]
#         s[i]=cmd[0]
#         if cmd[1]==2: break
#         i += cmd[1]
#         q = cmd[2]
#     return ''.join(s)

# print(mt(30*'1'+45*'0').count('1'))


# command = {
#     (' ',0): (' ',-1,1),
#     (' ',2): (' ',2,2),
#     (' ',3): (' ',2,3),
#     ('0',1): ('1',-1,2),
#     ('0',2): ('1',-1,2),
#     ('0',3): ('0',-1,3),
#     ('1',1): ('0',-1,2),
#     ('1',2): ('1',-1,3),
#     ('1',3): ('0',-1,2)
# }

# def mt(s):
#     s = list(' '+s+' ')
#     q = 0
#     i = len(s)-1
#     while True:
#         cmd = command[(s[i],q)]
#         s[i]=cmd[0]
#         if cmd[1]==2: break
#         i += cmd[1]
#         q = cmd[2]
#     return ''.join(s)

# print(int(mt(f'{992:b}'),2))


# command = {
#     (' ',0): (' ',1,1),
#     ('0',1): ('2',1,1),
#     ('1',1): ('0',2,1),
#     ('2',1): ('1',1,1)
# }

# def mt(s):
#     s = list(' '+s+' ')
#     q = 0
#     i = 0
#     while True:
#         cmd = command[(s[i],q)]
#         s[i]=cmd[0]
#         if cmd[1]==2: break
#         i +=cmd[1]
#         q=cmd[2]
#     return ''.join(s)

# s = mt(323*'2'+115*'0'+562*'1').replace(' ', '0')
# print(sum(map(int, s)))


# command = {
#     (' ',0): (' ',-1,1),
#     (' ',1): (' ',2,2),
#     (' ',2): (' ',2,3),
#     ('0',1): ('5',-1,2),
#     ('0',2): ('x',-1,1),
# }

# def mt(s):
#     s = list(' '+s+' ')
#     q = 0
#     i = len(s)-1
#     for x in range(0,1000):
#         while True:
#             cmd = command[(s[i],q)]
#             s[i]=cmd[0]
#             if cmd[1]==2: break
#             i +=cmd[1]
#             q=cmd[2]
#         return ''.join(s)

# s = mt(323*'2'+115*'0'+562*'1').replace(' ', '0')
# print(sum(map(int, s)))


# command = {
#     (' ',0): (' ',1,1),
#     (' ',1): ('1',1,2),
#     (' ',2): ('0',1,3),
#     (' ',3): (' ',2,3),
#     ('0',1): ('1',1,1),
#     ('1',1): ('0',1,1),
# }

# def mt(s):
#     s = list(' '+s+' ')
#     q = 0
#     i = len(s)-1
#     while True:
#         cmd = command[(s[i],q)]
#         s[i]=cmd[0]
#         if cmd[1]==2: break
#         i+=cmd[1]
#         q=cmd[2]
#     return ''.join(s)

# print(mt(bin(32)[2:]))


command = {
    (' ',0): (' ',1,1),
    (' ',1): ('0',1,2),
    (' ',2): ('0',1,3),
    (' ',3): (' ',2,3),
    ('0',1): ('0',1,1),
    ('1',1): ('1',1,1),
}

def mt(s):
    s = list(' '+s+' ')
    q = 0
    i = len(s)-1
    while True:
        cmd = command[(s[i],q)]
        s[i]=cmd[0]
        if cmd[1]==2: break
        i+=cmd[1]
        q=cmd[2]
    return ''.join(s)

print(mt(bin(2028)[2:]))