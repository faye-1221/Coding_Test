# # 시간초과
# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [list(map(int, input().strip())) for _ in range(N)]

# def bfs(i, j, graph, N, M):
#     visit_graph = deque([(i, j)])
#     visited = []
#     result = 1
#     dist = [(1, 0), (0, 1), (0, -1), (-1, 0)]

#     while visit_graph:
#         x, y = visit_graph.popleft()
        
#         for dx, dy in dist:
#             nx = x+dx
#             ny = y+dy
#             if N > nx >= 0 and M > ny >= 0 and \
#                 graph[nx][ny] == 0 and \
#                     (nx, ny) not in visited:
#                 result += 1
#                 visited.append((nx, ny))
#                 visit_graph.append((nx, ny))
#     return result


# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             print(bfs(i, j, graph, N, M), end='')
#         else:
#             print(0, end='')
#     print()

# 플러드필? https://data-flower.tistory.com/86
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dist = [(1, 0), (0, 1), (0, -1), (-1, 0)]

# 구역 크기 계산 bfs
def bfs(x, y, zone_id):
    
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    zone_map[x][y] = zone_id

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dist:
            nx, ny = cx + dx, cy + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] \
                and graph[nx][ny] == 0:
                visited[nx][ny] = True
                zone_map[nx][ny] = zone_id
                size += 1
                queue.append((nx, ny))

    return size

visited = [[False] * M for _ in range(N)]
zone_map = [[-1] * M for _ in range(N)]
zone_sizes = []

zone_id = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            zone_size = bfs(i, j, zone_id)
            zone_sizes.append(zone_size)
            zone_id += 1

# 결과 계산
result = []
for i in range(N):
    row = []
    for j in range(M):
        if graph[i][j] == 1:
            adjacent_sum = 1
            visited_zones = set()
            for dx, dy in dist:
                nx, ny = i + dx, j + dy
                if N > nx >= 0 and M > ny >= 0 and graph[nx][ny] == 0:
                    zone = zone_map[nx][ny]
                    if zone not in visited_zones:
                        visited_zones.add(zone)
                        adjacent_sum += zone_sizes[zone]
            row.append(adjacent_sum % 10)
        else:
            row.append(0)
    result.append(row)

for row in result:
    print(''.join(map(str, row)))