n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1
for n in l:
    for j in range(n, k+1):
        dp[j] += dp[j-n]
print(dp[k])