from collections import deque
import sys
N = int(input())

de = deque()
for _ in range(N):
    s = sys.stdin.readline().split()
    com = s[0]

    if(com == "push_front"):
        de.appendleft(s[1])

    if(com == "push_back"):
        de.append(s[1])

    if(com == "pop_front"):
        if(len(de) == 0):
            print(-1)
        else:
            print(de.popleft())

    if(com == "pop_back"):
        if(len(de) == 0):
            print(-1)
        else:
            print(de.pop())
    
    if(com == "size"):
        print(len(de))

    if(com == "empty"):
        if(len(de) == 0):
            print(1)
        else:
            print(0)
    
    if(com == "front"):
        if(len(de) == 0):
            print(-1)
        else:
            print(de[0])
        
    
    if(com == "back"):
        if(len(de) == 0):
            print(-1)
        else:
            print(de[-1])
        
