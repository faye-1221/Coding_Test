import sys
K, N = map(int, input().split())
l = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(l)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in  l:
        result += int(i // mid)
    
    if result >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)