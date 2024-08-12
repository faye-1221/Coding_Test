from collections import defaultdict
import heapq
import sys

input = sys.stdin.read
data = input().split()

V, E = int(data[0]), int(data[1])
K = int(data[2])

graph = defaultdict(list)
index = 3

for _ in range(E):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    graph[u].append((v, w))
    index += 3

INF = float('inf')
dist = [INF] * (V + 1)
dist[K] = 0

Q = [(0, K)]

while Q:
    time, node = heapq.heappop(Q)

    if time > dist[node]: # 더 긴 경로가 큐에 있을 경우
        continue

    for v, w in graph[node]:
        alt = time + w
        if alt < dist[v]:
            dist[v] = alt
            heapq.heappush(Q, (alt, v))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
