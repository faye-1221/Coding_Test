from collections import deque

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

# 좌표 저장
queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 정답이 담길 변수
res = 0

# 위치 자표를 append
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            # 좌표가 크기를 넘지 않고, 익지 않은 상태이면
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in matrix:
    for j in i:
        # 토마토가 익지 못했다면 -1
        if j == 0:
            print(-1)
            exit(0)
    
    # 다 익었으면 최댓값이 정답
    res = max(res, max(i))


print(res-1)