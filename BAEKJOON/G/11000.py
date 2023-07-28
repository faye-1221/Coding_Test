import sys
import heapq
N = int(sys.stdin.readline()) # 강의실 개수

time = []
heap = []
for i in range(N):
    S, T = map(int, sys.stdin.readline().split()) # start, stop 시간
    
    time.append((S, T))

time = sorted(time, key=lambda x:(x[0], x[1]))

heapq.heappush(heap, time[0][1])

for t in time[1:]:
    if t[0] < heap[0]:
        heapq.heappush(heap, t[1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, t[1])

print(len(heap))