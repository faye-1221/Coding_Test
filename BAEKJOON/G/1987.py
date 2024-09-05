# python3: 시간 초과, pypy: 메모리 초과
# from collections import deque

# R, C = map(int, input().split())
# graph = [list(input()) for _ in range(R)]

# queue = deque([(0, 0, graph[0][0])])
# visited = set([(0, 0, graph[0][0])]) 

# max_count = 1 

# while queue:
#     x, y, path = queue.popleft() # dfs
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in path:
#             new_path = path + graph[nx][ny]
#             queue.append((nx, ny, new_path))
#             visited.add((nx, ny, new_path))
#             max_count = max(max_count, len(new_path))

# print(max_count)

from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

queue = deque([(0, 0, graph[0][0])])
visited = [[set() for _ in range(C)] for _ in range(R)]
visited[0][0].add(graph[0][0]) 

max_count = 1 

while queue:
    x, y, path = queue.popleft() # dfs
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in path:
            new_path = path + graph[nx][ny] # 현재 지나온 경로 path에 추가

            if new_path not in visited[nx][ny]: # 새로운 경로인지 확인
                queue.append((nx, ny, new_path))
                visited[nx][ny].add(new_path)
                max_count = max(max_count, len(new_path))

print(max_count)