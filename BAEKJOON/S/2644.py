from collections import deque
n = int(input()) # 전체 사람의 수
start, end = map(int, input().split()) # 촌수 계산해야하는 사람 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

graph = [[] for _ in range(n+1)]

# 부모 자식간의 관계
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

def bfs(start, end):
    visited = [False] * (n+1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        current, count = queue.popleft()

        if current == end:
            return count
    
        for v in graph[current]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, count+1))
    return -1

print(bfs(start, end))