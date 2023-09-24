import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
ans = []
visited = [False] * n

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    remember_num = 0
    for i in range(n):
        print(remember_num != nums[i])
        if not visited[i] and remember_num != nums[i]:
            visited[i] = True # 방문
            remember_num = nums[i] # 해당 숫자 중복 불가능
            ans.append(nums[i]) # 추가
            back()
            visited[i] = False
            ans.pop()
back()