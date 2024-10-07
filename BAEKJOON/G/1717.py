import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n, m = map(int, input().split())
root = list(range(n+1))

def find(x):
    if root[x] != x:
        root[x] = find(root[x])  # 경로 압축
    return root[x]

def same_set(b, c):
    if find(b) == find(c):
        print("YES")
    else:
        print("NO")

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        same_set(b, c)