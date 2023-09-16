from collections import deque
import sys

N = int(sys.stdin.readline())
result = deque()

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    
    if len(l) == 2:
        result.append(l[-1])
    else:
        if l[0] == 2:
            if result:
                print(result.pop())
            else:
                print(-1)
        elif l[0] == 3:
            print(len(result))
        elif l[0] == 4:
            if result:
                print(0)
            else:
                print(1)
        elif l[0] == 5:
            if result:
                print(result[-1])
            else:
                print(-1)
