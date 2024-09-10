N, K = map(int, input().split())
l = list(map(int, input().split()))
dist = []
for i in range(N-1):
    dist.append(l[i+1] - l[i])

dist.sort(reverse=True)

print(sum(dist[K-1:]))