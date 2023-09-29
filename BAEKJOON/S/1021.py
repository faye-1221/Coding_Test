from collections import deque
N, M = map(int, input().split())
nums = deque(map(int, input().split()))

q = deque(i for i in range(1, N+1))
result = 0

while nums:
    idx = q.index(nums[0])
    
    # 왼쪽으로 도는게 가까울 때
    if len(q)//2 < idx:
        while q[0] != nums[0]:
            q.rotate(1)
            result += 1
        q.popleft()
    # 오른쪽으로 도는게 가까울 때
    else:
        while q[0] != nums[0]:
            q.rotate(-1)
            result += 1
        q.popleft()
    nums.popleft()

print(result)