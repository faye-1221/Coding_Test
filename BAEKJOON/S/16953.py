# a, b = map(int,input().split())
# result = 1

# # 거꾸로 하면
# # 2로 나누기, 홀수일 때 x
# # 1 제거

# while(b!=a):
#     result += 1
#     temp = b
#     if b%10 == 1:
#         b//=10
#     elif b%2 == 0:
#         b//=2
    
#     if temp == b:
#         print(-1)
#         break
# else:
#     print(result)

# BFS
from collections import deque

def bfs(A, B):
    queue = deque([(A, 1)])  # (현재 값, 연산 횟수)
    
    while queue:
        current, count = queue.popleft()
        
        # B에 도달한 경우
        if current == B:
            return count
        
        # 연산 1: 2를 곱하는 경우
        if current * 2 <= B:
            queue.append((current * 2, count + 1))
        
        # 연산 2: 1을 추가하는 경우
        if current * 10 + 1 <= B:
            queue.append((current * 10 + 1, count + 1))
    
    # B에 도달할 수 없는 경우
    return -1

A, B = map(int, input().split())
print(bfs(A, B))