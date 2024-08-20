import sys
input = sys.stdin.readline

N = int(input())

l = []

for _ in range(N):
    x, y = map(int, input().split())
    l.append((x, 1))
    l.append((y, -1))

# 좌표가 같으면 끝점(-1)이 시작점(1)보다 우선
l.sort()

current_active = 0
max_active = 0

for _, event_type in l:
    current_active += event_type
    max_active = max(max_active, current_active)

print(max_active)