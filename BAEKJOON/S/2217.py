# 로프를 병렬로 연결하면 각 로프에는 w/k만큼의 동일한 중량이 걸린다.
# 즉, 가장 작은 무게를 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게
# [100, 80, 60, 40, 20] -> [100*1, 80*2, 60*3, 40*4, 20*5]의 큰 값이 정답이다.

n = int(input())
k = []

for _ in range(n):
    k.append(int(input()))
k.sort()

answers = []
for x in k:
    answers.append(x*n)
    n -= 1
print(answers)
print(max(answers))