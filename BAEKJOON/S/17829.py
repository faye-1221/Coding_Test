n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]
result = []

def sol(n, x, y):
    mid = n//2
    if n==2:
        answer = [l[x][y], l[x+1][y], l[x][y+1], l[x+1][y+1]]
        return sorted(answer)[2]
    lt = sol(mid, x, y)
    rt = sol(mid, x+mid, y)
    lb = sol(mid, x, y+mid)
    rb = sol(mid, x+mid, y+mid)
    answer = [lt, rt, lb, rb]
    return sorted(answer)[2]

print(sol(n, 0, 0))