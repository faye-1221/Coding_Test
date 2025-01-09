# 시간초과-BFS
# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())

# queue = deque([(N, [N])])

# while queue:
#     X, path = queue.popleft()

#     if X == 1:
#         print(len(path)-1)
#         print(' '.join(map(str, path)))
#         break

#     if X % 3 == 0:
#         queue.append((X//3, path + [X//3]))

#     if X % 2 == 0:
#         queue.append((X // 2, path + [X // 2]))

#     queue.append((X - 1, path + [X - 1]))

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque([(N, [N])])
visited = set()

while queue:
    X, path = queue.popleft()

    if X == 1:
        print(len(path) - 1)
        print(' '.join(map(str, path)))
        break

    if X not in visited:
        visited.add(X)
        
        if X % 3 == 0:
            queue.append((X // 3, path + [X // 3]))

        if X % 2 == 0:
            queue.append((X // 2, path + [X // 2]))

        queue.append((X - 1, path + [X - 1]))

# DP: https://onn5.tistory.com/16: dp가 더 빠르다