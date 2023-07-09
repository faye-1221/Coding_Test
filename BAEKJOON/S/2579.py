# https://bio-info.tistory.com/158
n = int(input())
s = [int(input()) for _ in range(n)]  # 계단 리스트 다 저장

dp = [0] * (n) # dp 리스트 만들기

if len(s) <= 2: # 계단이 2개 이하일 때 다 덧셈
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    for i in range(2, n):
        # dp[i-3]에서 i가 2일때는 어차피 초기화된 0을 가져옴..!
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
    print(dp[-1])