# from itertools import product, permutations

# def f(x, y, w, z):
#     # ((w → y) → x) ˅ ¬z
#     return (not(not(w) or y) or x) or not(z)

# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
#     t = (
#         (x1, x2, 1, x3, 0),
#         (x4, 0, x5, x6, 0),
#         (x7, 1, 0, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations("xywz", r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in t):
#                 print(*p)

# def f(x, A):
#     return ((x % 7 != 0) and (x % 13 == 0)) <= ( x > A - 40)

# print(max(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, A):
#     return (x % A == 0) or ((40<=x<=50) <= (x % 12 != 0))

# print(max(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, A):
#     return (x&57 == 0) or ((x&23 == 0) <= (x&A != 0))

# print(min(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x, y, A):
#     return (x- y >= 39) or (y <= x) or (y >= A - 20)

# print(max(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     M = 32 <= x <= 68
#     N = 54 <= x <= 76
#     A = 0
#     f = (not (M or N)) == (not A)
#     if f != 1:
#         print(x)

# def f(x, y, A):
#     return (x <= 19) or (y < 2 * x + A - 50) or (y > 17)

# print(min(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 15 <= x <= 40
#     Q = 21 <= x <= 63
#     A = 0
#     f = P <= ((Q and (not A)) <= (not P))
#     if f != 1:
#         print(x)

# def f(x, y, A):
#     return (x + y <= 24) or (y <= x - 2) or (y >= A)

# print(max(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

# def f(x, y, A):
#     return (x + y <= 30) or (y <= x + 2) or (y >= A)

# print(max(A for A in range(1, 200) if all(f(x, y, A) == 1 for x in range(1, 2000) for y in range(1, 2000))))

def f(x, A):
    return (x % A == 0) or ((70 <= x <= 90) <= (not x % 22 == 0))

print(max(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 2000))))