# BFS
from collections import deque
n, m = map(int, input().split())
start_x, start_y  = 0, 0
graph =  []

for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)
    if 2 in l:
        start_x = i
        start_y = l.index(2)
        graph[start_x][start_y] = 0

def bfs(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, dist = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < end_x and 0 <= ny < end_y:
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist+1))
                        graph[nx][ny] = dist+1

    # 도달할 수 없는 지점을 '-1'!!!
    for i in range(end_x):
        for j in range(end_y):
            if graph[i][j] == 1 and (i, j) not in visited:
                graph[i][j] = -1

    for i in graph:
        print(*i)

bfs(start_x, start_y, n, m, graph)

'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''