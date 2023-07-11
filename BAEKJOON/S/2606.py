def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    if v in com.keys():
        for w in com[v]:
            if w not in discovered:
                discovered = recursive_dfs(w, discovered)
    return discovered

computer_n = int(input())
pair = int(input())

com = {}
for _ in range(pair):
    one, two = map(int, input().split())
    com[one] = com.get(one, []) + [two]
    com[two] = com.get(two, []) + [one]

print(len(recursive_dfs(1))-1)