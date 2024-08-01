from itertools import permutations
# 1~9까지 서로 다른 숫자 세개
# 같은 자리/같은 숫자: 스트라이크
# 다른 자리/같은 숫자: 볼
# 3 스트라이크면 종료 아니면 다시
# 영수의 답이 입력으로 주어질 때 가능성 있는 답의 총 개수

# ball_num에 영수의 숫자가 맞으면 True
# true_num에 자리를 찾은 숫자를 append
# true_num에 없는데 ball_num인 조합을 계산하면 나오지 않을까???
T = int(input())
ball_num = [False for _ in range(9)] # 볼이면 True
true_num = []

for _ in range(T):
    n, strike, ball = map(int, input().split())
    