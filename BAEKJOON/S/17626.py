# import sys

# n = int(sys.stdin.readline())

# i = 1
# dp = [i]

# while dp[-1] <= n:
#     i += 1
#     dp.append(i * i)

# print(len(dp))
# cnt = []

# def find(n):
#     global cnt
    

#     if n in dp:
#         cnt.append(n)
#     else:
#         smaller_values = list(filter(lambda x: x < n, dp))
#         result = max(smaller_values)
#         cnt.append()
#         find(n - result)
#     return
#     # for i in range(1, len(dp)+1):
#     #     if dp[i-1] == 0:
#     #         dp[i-1] = i * i

#     #     if n == dp[i-1]:
#     #         cnt += 1
#     #         return cnt
        
#     #     if dp[i-1] > n:
#     #         cnt += 1
#     #         break            
#     # cnt = find(n - dp[i-2])
#     # return cnt
# find(n)
# print(cnt)

# https://lighter.tistory.com/7
# 17626번 Four Squares
# DP
n = int(input())

i = 1

# square_num_li = [i*i for i in range(1, 224)]
square_num_li = [i]
while square_num_li[-1] <= n:
    i += 1
    square_num_li.append(i * i)

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i in square_num_li:
        dp[i] = 1 # 안에 있으면 그냥 dp를 1로 저장
    else:
        dp[i] = min([dp[i-j] for j in square_num_li if i-j > 0])+1
    
        
print(dp[n])