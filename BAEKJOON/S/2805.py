import sys
K, M = map(int, input().split())
l = list(map(int, input().split()))

start, end = 1, max(l)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in l:
        if i >= mid:
            result += i - mid
    
    if result >= M:
        start = mid + 1
    else:
        end = mid -1
print(end)