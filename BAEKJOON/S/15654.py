n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in nums:
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()

back()