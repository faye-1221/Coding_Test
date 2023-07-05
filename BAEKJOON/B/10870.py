# 재귀
# def fib(n):
#     if n <= 1:
#         return n
#     n = fib(n-1) + fib(n-2)
#     return n

# n = int(input())
# print(fib(n))

# 메모라이즈
import collections

dp = collections.defaultdict(int)

def fib(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
    
n = int(input())
print(fib(n))