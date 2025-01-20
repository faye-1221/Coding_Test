T = int(input())

for i in range(T):
    N = int(input()) # 동전의 수
    N_list = list(map(int, input().split())) # 동전 오름차순
    M = int(input()) # 만들어야하는 금액

    # N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한줄에 하나씩
    dp = [0] * (M+1)
    dp[0] = 1
    for n in N_list:
        for j in range(n, M+1):
            dp[j] += dp[j-n]
    print(dp[M])