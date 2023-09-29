size = int(input())
nums = list(map(int, input().split()))

for i in range(1, size):
    nums[i] = max(nums[i], nums[i]+nums[i-1])
print(max(nums))