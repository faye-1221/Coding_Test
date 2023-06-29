N, M = map(int, input().split())
n = []
m = []

for _ in range(N):
    n.append(input())

for _ in range(M):
    m.append(input())

for i in m:
    if i.isdigit():
        print(n[int(i)-1])
    else:
        print(n.index(i) + 1)
