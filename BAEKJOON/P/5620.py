import math
n = int(input())

l = []
for _ in range(n):
    x, y = map(int, input().split())
    
    l.append((x, y))

# 루트((a_1-b_1)^2 + (a_2-b_2)^2))
def func(p1, p2):
    return int(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

l.sort()

result = int(1e10)

start = l[0]

for i in range(1, n):
    result = min(result, func(start, l[i]))

print(result**2)