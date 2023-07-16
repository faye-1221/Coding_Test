N, M = map(int, input().split())

l = []
l2 = []
for i in range(N):
    l.append(list(map(int, input().split())))

for i in range(N):
    l2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(l[i][j] + l2[i][j], end=" ")
    print()