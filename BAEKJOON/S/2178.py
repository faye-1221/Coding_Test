from collections import deque
N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input())))
visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(maps, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    distance = {(x, y): 0}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:

        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and maps[nx][ny]:
                if (nx, ny) == (N-1, M-1): return distance[(x, y)] + 2
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                visited[nx][ny] = True

    return -1

print(bfs(maps, 0, 0, visited))