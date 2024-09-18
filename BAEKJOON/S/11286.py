import heapq
import sys
input = sys.stdin.readline

q = []

N = int(input())

for _ in range(N):
    n = int(input())
    if n == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(n), n))