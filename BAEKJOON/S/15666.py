import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
ans = []

def back(start = 0):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    remember_num = 0
    for i in range(start, n):
        if remember_num != nums[i]:
            remember_num = nums[i] # 해당 숫자 중복 불가능
            ans.append(nums[i]) # 추가
            back(i)
            ans.pop()
back()