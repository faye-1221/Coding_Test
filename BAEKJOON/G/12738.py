import bisect

target = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(target):
    if nums[i] > dp[-1]:
        dp.append(nums[i])
    else:
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]
print(len(dp))