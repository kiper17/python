#1.1
n = int(input())
for i in range(1,n+1):
    a = 0
    for j in range(1,n+1):
        if i%j==0:
            a+=1
    if a==2:
        print(i)


#1.2
N = int(input())

# Создается список из значений от 0 до N включительно
primes = [i for i in range(N + 1)]

# Вторым элементом списка является единица, которую
# не считают простым числом. Забиваем ее нулем
primes[1] = 0

# Начинаем с 3-го элемента
i = 2
while i <= N:
    # Если значение текущей ячейки до этого не было обнулено,
    # значит в этой ячейке содержится простое число
    if primes[i] != 0:
        # Первое кратное ему будет в два раза больше
        j = i + i
        while j <= N:
            # и это число составное,
            # поэтому заменяем его нулем
            primes[j] = 0
            # переходим к следующему числу,
            # которое кратно i (оно на i больше)
            j = j + i
    i += 1

# Избавляемся от всех нулей в списке
primes = [i for i in primes if i != 0]
print(primes)

#43
# Открываем входной файл
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().lower().split()

# Создаём словарь для подсчёта слов
words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Записываем результат в выходной файл
with open("output.txt", "w", encoding="utf-8") as f:
    for word in sorted(words):
        f.write(word + " " + str(words[word]) + "\n")


#44
expr = input("Введите выражение в постфиксной форме: ")

stack = []

tokens = expr.split()

for token in tokens:
    if token.isdigit():  # если число
        stack.append(int(token))
    else:  # если оператор
        b = stack.pop()
        a = stack.pop()
        
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            stack.append(a / b)

# Результат — последний элемент стека
print("Результат:", stack.pop())

#46
expr = input("Введите выражение: ")

stack = []
ok = True

for ch in expr:
    if ch == '(' or ch == '[' or ch == '{' or ch == '<':
        stack.append(ch)

    elif ch == ')':
        if not stack or stack[-1] != '(':
            ok = False
            break
        stack.pop()

    elif ch == ']':
        if not stack or stack[-1] != '[':
            ok = False
            break
        stack.pop()

    elif ch == '}':
        if not stack or stack[-1] != '{':
            ok = False
            break
        stack.pop()

    elif ch == '>':
        if not stack or stack[-1] != '<':
            ok = False
            break
        stack.pop()

if ok and not stack:
    print("Правильно")
else:
    print("Неправильно")