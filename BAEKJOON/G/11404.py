# n개의 도시, 한 도시에서 출발해서 도착하는 m개의 버스
# (A, B) 도시 A에서 B로 가는데 필요한 비용의 최솟값

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

inf = float('inf')
dist = [[inf] * n for _ in range(n)]

for i in range(n): # 자기자신
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a-1][b-1]: # 이미 저장된 것이라면 가장 작은 값을 저장
        dist[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

# 출력
for i in range(n):
    for j in range(n):
        if dist[i][j] == inf:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()