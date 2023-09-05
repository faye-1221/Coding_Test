n = int(input())
array = [0]*10000

for i in range(n):
    array[i] = int(input())

dp = [0] * 10000

dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[2]+array[0], array[2]+array[1], dp[1])

for i in range(3, n):
    # https://www.acmicpc.net/board/view/60664
    # 1. 전전(n-2)까지의 최대 양 + 현재 양 = (dp[n-2] + wine[n])
    # 2. 전전전(n-3)까지의 최대 양 + 전(n-1)번째 양 + 현재 양 = (dp[n-3] + wine[n-1] + wine[n])
    dp[i] = max(array[i] + dp[i-2], array[i]+array[i-1]+dp[i-3], dp[i-1])

print(max(dp))