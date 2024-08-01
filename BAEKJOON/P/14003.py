import bisect

target = int(input())
nums = list(map(int, input().split()))

dp = []

mx = -1000000000

for i in range(target):
    if nums[i] > mx:
        dp.append(nums[i])
        mx = nums[i]
    else:
        idx = bisect.bisect_left(dp, nums[i])
        try:
            dp[idx] = nums[i]
        except IndexError:
            dp.append(nums[i])

print(len(dp))

for i in dp:
    print(i, end=' ')
