N = int(input())
positive = []
negative = []
result = 0

for _  in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    else:
        result += 1

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        result += positive[i] * positive[i+1]
    else:
        result += positive[i]

for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        result += negative[i] * negative[i+1]
    else:
        result += negative[i]
print(result)