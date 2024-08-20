import sys
input = sys.stdin.readline

N = int(input())

l = []

# 두 점의 위치 x, y (-1,000,000,000 ≤ x < y ≤ 1,000,000,000)
for _ in range(N):
    x, y = map(int, input().split())

    l.append((x, y))
    
l.sort()

ans = 0

start, end = l[0]

for i in range(1, N): 
    next_start, next_end = l[i]
    
    if next_start <= end: # 첫 번째 끝점이 두 번째 시작점보다 크거나 같으면 겹침
        end = max(end, next_end)
    else:
        ans += (end - start)
        start = next_start
        end = next_end

ans += (end-start)

print(ans)