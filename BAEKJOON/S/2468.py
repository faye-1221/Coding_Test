from collections import deque

def bfs(x, y, visited, data, N):
    queue = deque([(x, y)])
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and data[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

N = int(input())
max_num = 1
region = []

for _ in range(N):
    new_region = list(map(int, input().split()))
    region.append(new_region)
    max_num = max(max_num, max(new_region))

max_safe_areas = 0

# 높이는 1이상 100이하의 정수
# 높이 큰 수부터 1까지
for height in range(max_num + 1):
    data = [[value > height for value in row] for row in region]
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0

    for x in range(N):
        for y in range(N):
            if data[x][y] and not visited[x][y]:
                bfs(x, y, visited, data, N)
                safe_areas += 1
    
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)