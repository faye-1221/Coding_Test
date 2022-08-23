import math

N = int(input())
cnt = 0

l = list(map(int, input().split(' ')))
for i in l:
    i_error = 0
    if i > 1:  # 1은 소수가 아님
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                i_error += 1
        if i_error == 0:
            cnt += 1

print(cnt)
