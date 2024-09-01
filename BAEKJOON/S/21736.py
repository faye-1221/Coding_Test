from collections import deque
N, M = map(int, input().split())
# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐
# 도연이가 만날 수 있는 사람의 수를 출력한다.

start_x, start_y = 0, 0
graph = []
for i in range(N):
    l = list(input())
    if 'I' in l:
        start_x = i
        start_y = l.index('I')
    graph.append(l)

def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    rows, cols = len(graph), len(graph[0])

    cnt = 0 # 만나는 친구 횟수
    
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    
    while queue:
        row, col = queue.popleft()
    
        if graph[row][col] == 'P':
            cnt += 1
    
        for i in range(4):
            next_row = row + dx[i]
            next_col = col + dy[i]
            
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if (next_row, next_col) not in visited:

                    if graph[next_row][next_col] == 'P' or graph[next_row][next_col] == 'O':
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
                    else:
                        visited.add((next_row, next_col))
    if cnt == 0:
        print('TT')
    else:
        print(cnt)

bfs(start_x, start_y, graph)