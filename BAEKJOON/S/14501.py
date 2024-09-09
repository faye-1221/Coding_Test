N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    if i + l[i][0] <= N: # 상담이 가능
        dp[i + l[i][0]] = max(dp[i + l[i][0]], dp[i] + l[i][1])
    dp[i + 1] = max(dp[i + 1], dp[i]) 
    # print(dp)

print(dp[N])