import sys
from collections import deque

N = int(input())

queue = deque()
for _ in range(N):
    w = sys.stdin.readline().split()
    com = w[0]
    
    if com == "push":
        queue.append(w[1])

    if com == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    if com == "size":
        print(len(queue))
    
    if com == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if com == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if com == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    