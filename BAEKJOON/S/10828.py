import sys
N = int(sys.stdin.readline())
l = []

for _ in range(N):
    w = sys.stdin.readline().split()
    
    com = w[0]
    
    if com == "push":
        l.append(w[1])
    
    if com == "pop":
        if len(l) == 0:
            print("-1")
        else:
            print(l.pop())

    if com == "size":
        print(len(l))
    
    if com == "empty":
        if len(l) == 0:
            print(1)
        else:
            print(0)

    if com == "top":
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])