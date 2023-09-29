import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0: # 덱을 왼쪽으로 회전시켜 해당 풍선이 pop 대상이 되도록 만든다.
        q.rotate(-(paper - 1))
    elif paper < 0: # 덱을 오른쪽으로 회전시켜 해당 풍선이 pop 대상이 되도록 만든다.
        q.rotate(-paper)

print(' '.join(map(str, ans)))