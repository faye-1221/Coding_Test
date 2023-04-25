from collections import Counter
N = int(input())
n = map(int, input().split())
v = int(input())

c = Counter(n)

if c.get(v) == None:
    print(0)
else:
    print(c.get(v))