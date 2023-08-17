n = int(input())

# 각 상자의 크기가 순서대로 주어진다.
l = list(map(int, input().split()))

dp = [0] * 1001

for i in range(n):
    dp[i] = 1

    for j in range(i):
        if l[i] > l[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))