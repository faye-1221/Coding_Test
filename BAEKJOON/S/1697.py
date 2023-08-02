from collections import deque

def bfs(start):
    deep = 0
    queue = deque([(start, deep)])
    visited[start] = True
    while queue:
        v = queue.popleft()
        if v[0] == k:
            return v[1]
        for op in operation:
            num = op(v[0])
            if 0 <= num <= 100000 and not visited[num]:
                queue.append((num, v[1]+1))
                visited[num] = True


operation = [
    lambda x: x-1,
    lambda x: x+1,
    lambda x: x*2,
]

n, k = map(int, input().split())

if (k < n):
    print(n-k)
else:
    visited = [False]*(100000+1)
    print(bfs(n))