N, M, V = map(int, input().split())

graph = {}
for i in range(M):
	a, b = map(int, input().split())
	graph[a] = graph.get(a, []) + [b]
	graph[b] = graph.get(b, []) + [a]

for key in graph:
    graph[key]  = sorted(graph[key])


def BFS(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        if v in graph.keys():
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
    return discovered


def DFS(v, discovered=[]):
    discovered.append(v)
    if v in graph.keys():
        for w in graph[v]:
            if w not in discovered:
                discovered = DFS(w, discovered)
    return discovered

print(' '.join(map(str, DFS(V))))
print(' '.join(map(str, BFS(V))))