N, M = map(int, input().split())

l = {}
n_cnt = 0

def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    if v in l.keys():
        for w in l[v]:
            if w not in discovered:
                discovered = recursive_dfs(w, discovered)
    return discovered

l = {}
for _ in range(M):
    u, v = map(int, input().split())
    l[u] = l.get(u, []) + [v]
    l[v] = l.get(v, []) + [u]

l2 = []
v = 1
while N != len(l2):
    l2 = []
    dis = sorted(recursive_dfs(v))
    l2.extend(dis)
    l2 = list(set(l2))
    v = l2[-1] + 1
    n_cnt += 1
print(n_cnt)