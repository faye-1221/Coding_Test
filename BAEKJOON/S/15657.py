n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []

def back(start = 0):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(start, len(nums)):
        ans.append(nums[i])
        back(i)
        ans.pop()

back()