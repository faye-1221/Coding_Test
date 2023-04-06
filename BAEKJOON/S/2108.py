import sys
from collections import Counter
N = int(sys.stdin.readline())

l = list()

for i in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()

print(int(round(sum(l)/N, 0)))

print(l[N//2])

f = Counter(l)
b = f.most_common() 

if len(l) > 1:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(l[0])

print(l[-1] - l[0])