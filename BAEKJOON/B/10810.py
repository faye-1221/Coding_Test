N, M = map(int, input().split())

l = [0 for _ in range(N)]

for i in range(M):
    i, j, k = map(int, input().split())

    l[i-1:j] = [k for i in range(j-i+1)]

for i in l:
    print(i, end=' ')