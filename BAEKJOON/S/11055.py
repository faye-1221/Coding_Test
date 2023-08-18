N = int(input())
A = list(map(int, input().split()))

dp = [0]

for i in range(N):
    dp[i] += A[i]