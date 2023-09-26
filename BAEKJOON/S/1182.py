# N, S = map(int, input().split())
# arr = list(map(int, input().split()))

# cnt = 0

# def dfs(data, sol, level):
#     global cnt
#     if sol and sum(sol) == S:
#         cnt +=1
#         return

#     for i in range(level, N):
#         sol.append(data[i])
#         dfs(data, sol, i+1)
#         sol.pop()
        
# dfs(arr, [], 0)  
# print(cnt)

import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)