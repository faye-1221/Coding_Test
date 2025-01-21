MOD = 1000000009

t = int(input())
nums = [int(input()) for _ in range(t)] 

max_n = max(nums)

dp = [1, 2, 4]
for i in range(3, max_n):
    dp.append((dp[-3] + dp[-2] + dp[-1]) % MOD)

for n in nums:
    print(dp[n - 1])
