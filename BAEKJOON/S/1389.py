# # 플로이드-워셜: 비효율적....
n, m = map(int, input().split()) # 유저의 수, 관계의 수

INF = int(1e9)

graph = [[INF] * (n) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
graph = [sum(i) for i in graph]
print(graph.index(min(graph))+1)

# 다른 사람 코드
# from collections import deque

# # BFS 함수: start에서 다른 모든 사람까지의 최소 이동 거리를 계산
# def bfs(graph, start, n):
#     distances = [-1] * (n + 1)  # 모든 거리를 -1로 초기화
#     distances[start] = 0  # 시작점은 거리 0
#     queue = deque([start])
    
#     while queue:
#         current = queue.popleft()
        
#         for neighbor in graph[current]:
#             if distances[neighbor] == -1:  # 아직 방문하지 않은 노드라면
#                 distances[neighbor] = distances[current] + 1
#                 queue.append(neighbor)
    
#     return sum(distances[1:])  # 1번 인덱스부터 총 거리를 반환

# # 입력 받기
# n, m = map(int, input().split())  # n: 사람 수, m: 친구 관계 수
# graph = [[] for _ in range(n + 1)]  # 1번부터 n번까지 사용

# # 그래프 구성
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 각 사람의 케빈 베이컨 수 계산
# min_bacon = float('inf')
# person = 0

# for i in range(1, n + 1):
#     bacon_sum = bfs(graph, i, n)
#     if bacon_sum < min_bacon:
#         min_bacon = bacon_sum
#         person = i

# print(person)
