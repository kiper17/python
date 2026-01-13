M, N, K = map(int, input().split())

V = 200
W = 100

r = N % K

if r == 1:
    print(0)
elif N + K + 1 > M:
    print((r - 1) * V)
elif N < K + 1:
    print((N - 1) * V)
elif (r + 1) * V < (K + 1 - r) * W:
    print((r + 1) * V)
else:
    print((K + 1 - r) * W)