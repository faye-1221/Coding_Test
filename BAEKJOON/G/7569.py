# 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정, 토마토들이 다 익는 최소 일수
# 일부의 칸에 없을 수도, 1은 익음, 0은 익지 않음, -1은 없음
from collections import deque

M, N, H = map(int, input().split())  # 가로 칸의 수, 세로 칸의 수, 상자의 수
graph = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    graph.append(layer)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(graph):
    queue = deque()
    # 초기 익은 토마토를 큐에 모두 추가
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if graph[z][x][y] == 1:
                    queue.append((z, x, y))
    
    while queue:
        z, x, y = queue.popleft()
        
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if graph[nz][nx][ny] == 0:  # 안 익은 토마토
                    graph[nz][nx][ny] = graph[z][x][y] + 1 # 날짜 기록
                    queue.append((nz, nx, ny))
    # print(graph)
    
    days = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if graph[z][x][y] == 0:  # 안 익은 토마토가 있으면 바로 -1
                    return -1
                days = max(days, graph[z][x][y])
    
    return days - 1

print(bfs(graph))
