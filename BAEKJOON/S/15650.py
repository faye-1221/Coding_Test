# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
# 오름차순
n, m = map(int, input().split())
ans = []

def back(start=1):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            back(i)
            ans.pop()
back()