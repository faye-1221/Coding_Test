N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
dp = [0 for _ in range(N+1)]

for i in range(1, N+1): # 구매하려는 카드 수
    for j in range(1, i+1): # 현재 선택할 카드 크기
        dp[i] = max(dp[i], P[j] + dp[i-j]) # i장을 만들 수 있는 최대 가격 산출

print(dp[N])
