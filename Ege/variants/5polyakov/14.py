
x = 30 * 36**231 + 18 * 6**101 - 3 * 36**45 - 2357

digits = []
while x > 0:
    digits.append(x % 36)
    x //= 36

count = 0
for d in digits:
    if (d % 3 == 0 or d % 5 == 0) and not (d % 3 == 0 and d % 5 == 0):
        count += 1

print(count)