# backtracking
n, m = map(int, input().split())
ans = []

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(1, n+1): # 1~N까지
        if i not in ans: # 중복 확인
            ans.append(i)
            back() # 재귀
            ans.pop() # 1, 2, 3일 때 3을 없앰으로 전 단계로 돌아감
back()

# 파이썬 내장 함수(메모리 동일, 속도는 빠름)
# from itertools import permutations
# n, m = map(int, input().split())
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(" ".join(map(str, i)))