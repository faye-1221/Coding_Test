# 약수들의 누적합을 구하는 문제이다.
# 주어진 입력이 1~1000000의 수로 제한되어 있어서 해당 수의 약수를 구한 뒤, 이 약수들의 누적합을 담고
# 입력이 주어질 때 마다 해당 배열에서 출력하는 방식이다.

import sys

input = sys.stdin.readline
MAX = 1000001

# 약수 구하기
divisor = [0] * MAX
divisor[1] = 1

for i in range(2, MAX):
    for j in range(1, i+1):
        if i * j < MAX:
            if i == j:
                divisor[i*j] += j
            else:
                divisor[i*j] += j+i
        else:
            break

# 누적합 구하기
ans = [0] * MAX
for i in range(1, MAX):
    ans[i] += divisor[i] + ans[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(ans[n])