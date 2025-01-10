# 틀린답
# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [9]

# for n in range(1, N):
#     dp.append(
#         (dp[n-1] - n) * 2 + n
#     )

# print(dp[n]%1000000000)

# 그냥 무식하게 채우기
# import sys
# input = sys.stdin.readline

# N = int(input())

# dp = [[0] * 10 for _ in range(N+1)]

# for i in range(1, 10):
#     dp[1][i] = 1

# for n in range(2, N+1):
#     for last in range(10):
#         if last > 0:
#             dp[n][last] += dp[n-1][last-1]
        
#         if last < 9:
#             dp[n][last] += dp[n - 1][last + 1]
#         dp[n][last] %= 1000000000

# result = sum(dp[N]) % 1000000000
# print(result)

# 행렬 거듭 제곱
MOD = 1000000000

def mat_mul(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= MOD
    return result

def mat_pow(mat, exp):
    size = len(mat)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]  # 단위 행렬
    while exp:
        if exp % 2 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        exp //= 2
    return result

# 0에서 1로 전이가 가능하고
# 1에서 0, 2/ 2에서 1, 3이 가능한 것을 토대로 전이 행렬 T를 정의
T = [[0] * 10 for _ in range(10)]
for i in range(10):
    if i > 0:
        T[i][i-1] = 1
    if i < 9:
        T[i][i+1] = 1

N = int(input())
if N == 1:
    print(9)
    exit()

V1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

T_exp = mat_pow(T, N-1)

result = 0
for i in range(10):
    for j in range(10):
        result += V1[i] * T_exp[i][j]
        result %= MOD

print(result)

# 큰 N이면 행렬거듭제곱이 빠르겠지만 문제 자체는 N은 100이 최대라 dp