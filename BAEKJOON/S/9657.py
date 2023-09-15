N = int(input())

dp = ["SK", "SK", "CY", "SK", "SK"]

for i in range(5, N+1):
    if dp[i-1] + dp[i-3] + dp[i-4] == "SKSKSK":
        dp.append("CY")
    else:
        dp.append("SK")
    
print(dp[N])