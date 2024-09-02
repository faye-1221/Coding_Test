# 가중치 없는 방향 그래프 G가 주어졌을 때
# 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성

# i번째의 줄의 j번째 숫자가 1인 경우 i에서 j로 가는 간선이 존재, 0일 경우 없다는 뜻
# i번째 줄의 i번째 숫자는 항상 0

# 출력
# N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력, 정점 i에서 j로 가는 길이가 양수인 경로가 있으면
# i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력

# 플로이드-워셜 https://chanhuiseok.github.io/posts/algo-50/
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()

# dfs, bfs
# https://whitehairhan.tistory.com/333