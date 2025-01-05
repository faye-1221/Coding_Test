# https://velog.io/@himi/%EB%B0%B1%EC%A4%80-10942.-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC
import sys
input = sys.stdin.readline

# 입력받을 숫자의 개수
n = int(input())

# dp 테이블 생성: n x n 크기의 2차원 리스트로 초기값은 모두 False
dp = [[False] * n for i in range(n)]

# 주어진 숫자 리스트
num = list(map(int, input().split()))

# dp 테이블을 채우는 반복문
for idx in range(n):  # 길이를 나타내는 변수 (idx는 0부터 시작)
    for start in range(n):  # 시작 위치
        end = start + idx  # 끝 위치는 시작 위치 + 길이
        if end >= n:  # 끝 위치가 범위를 벗어나면 break
            break

        # 길이가 1인 경우 (idx == 0), 항상 팰린드롬이므로 True
        if idx == 0:
            dp[start][end] = True
            continue
            
        # 길이가 2인 경우 (idx == 1), 두 숫자가 같으면 팰린드롬
        if idx == 1:
            if num[start] == num[end]:
                dp[start][end] = True
                continue

        # 길이가 3 이상인 경우, 양 끝 숫자가 같고 안쪽 구간도 팰린드롬일 때 True
        if num[start] == num[end] and dp[start+1][end-1]:
            dp[start][end] = True

m = int(input())

for i in range(m):
    a, b = map(int, input().split())  # (1-based index)
    if dp[a-1][b-1]:  # dp 테이블은 0-based index이므로 a, b에서 1씩 뺌
        print(1)  # 팰린드롬이면 1 출력
    else:
        print(0)  # 팰린드롬이 아니면 0 출력
