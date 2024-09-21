N, M, K = map(int, input().split())
# 여학생 수, 남학생 수, 인턴쉽 참여자 수
# 2명, 1명으로 결성

result = 0

while N >= 2 and M >= 1 and N + M >= K + 3:
    N-=2
    M-=1
    result+=1
print(result)