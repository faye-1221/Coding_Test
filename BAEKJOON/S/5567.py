from collections import defaultdict, deque
n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = 0

def bfs(start):
    global result
    queue = deque([start])
    visited[start] = True
    level = 0

    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
                    if level < 2:
                        result += 1

        level += 1
        if level > 2:
            break

bfs(1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
print(result)