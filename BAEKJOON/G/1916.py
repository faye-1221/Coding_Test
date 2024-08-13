from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = defaultdict(list)

for _ in range(M):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))

start, end = map(int, input().split())

dist = defaultdict(int)

Q = [(0, start)]

while Q:
    time, node = heapq.heappop(Q)

    if node not in dist:
        dist[node] = time
        for e, v in graph[node]:
            alt = time + v
            heapq.heappush(Q, (alt, e))

print(dist[end])