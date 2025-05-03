import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]

result = 0
for _ in range(P):
    gate = int(input())
    root = find(gate) # 가장 가까운 빈 게이트를 찾음
    if root == 0: # 도킹할 수 있는 게이트가 없음 -> 종료
        break
    union(root, root - 1) # 아니면 도킹(union)
    result += 1

print(result)
