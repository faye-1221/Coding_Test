import sys
N, M = map(int, sys.stdin.readline().split())

S = set()

for i in range(N):
    S.add(sys.stdin.readline())

s = 0

for i in range(M):
    n = sys.stdin.readline()
    if n in S:
        s += 1
    
print(s)