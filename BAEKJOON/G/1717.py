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
        
'''
https://developer-project.tistory.com/435
import sys

n, m = map(int, sys.stdin.readline().split())

li = [i for i in range(n + 1)]

def union(a, b):
    if (find(a) != find(b)):
        li[find(b)] = find(a)

def find(a):
    if (li[a] == a):
        return a
    else:
        li[a] = find(li[a])
        return li[a]
    
def check(a, b):
    return (find(a) == find(b))

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())

    if (op == 0):
        union(a, b)
    else:
        if (check(a, b)):
            print('YES')
        else:
            print('NO')
'''