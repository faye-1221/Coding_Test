# from collections import deque

# N = int(input())
# graph, diff_graph = [], []
    
# for _ in range(N):
#     row = list(input())
#     graph.append(row)
#     diff_graph.append([char.replace('R', 'G') for char in row])

# def bfs(graph):
#     N, M = len(graph), len(graph[0])
#     dist = [[0 for _ in range(M)] for _ in range(N)]
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     visited = set([(0, 0)])
#     queue = deque([(0, 0)])

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if (nx, ny) not in visited:
#                     if graph[x][y] == graph[nx][ny]:
#                         queue.appendleft((nx, ny))
#                         dist[nx][ny] = dist[x][y]
#                         visited.add((nx, ny))
#                     else:
#                         queue.append((nx, ny))
#                         dist[nx][ny] = dist[x][y] + 1                  
#     print(max(max(row) for row in dist) + 1, end = ' ')
# bfs(graph)
# bfs(diff_graph)


# 다른 사람 방식
# dfs로 먼저 같은 문자면 계속해서 방문하도록 함
# 이후에 방문하지 않은 곳을 카운트해서 계산하고 R, G를 같은 글자로 변경 후에 계산

# 수정
from collections import deque

N = int(input())
graph, diff_graph = [], []

for _ in range(N):
    row = list(input())
    graph.append(row)
    diff_graph.append([char.replace('R', 'G') for char in row])

def bfs(x, y, graph, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)])
    visited[x][y] = True
    color = graph[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True

def count_areas(graph): # 같은 지역 count
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, graph, visited)
                count += 1

    return count

print(count_areas(graph), count_areas(diff_graph))
