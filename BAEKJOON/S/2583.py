from collections import deque
M, N, K = map(int, input().split())

paper = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            paper[M-1-i][j] = 1

def bfs(x, y, visited, paper, M, N):
    queue = deque([(x, y)])
    visited[x][y] = 1
    area = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        area += 1
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and paper[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))  
    return area

areas = []

for i in range(M):
    for j in range(N):
        if not visited[i][j] and paper[i][j] == 0:
            areas.append(bfs(i, j, visited, paper, M, N))

areas.sort()
print(len(areas))
print(*areas)  