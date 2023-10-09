# BFS.
# 1. 방문하지 않은 컴퓨터 중 작은 번화부터 BFS 수행
# 2. BFS가 끝나면 네트워크 개수 1 증가
# 3. 방문하지 않은 컴퓨터가 없을 때까지 1~2번을 반복 수행

from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start, visited, computers):
        visited[start] = True # 방문 체크
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for i in range(n):
                # 방문하지 않은 연결된 컴퓨터
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    # 방문하지 않은 컴퓨터 중 작은 번호부터 BFS 수행
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1

    return answer