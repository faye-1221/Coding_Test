import math

N, K = map(int, input().split(' '))
l = list()
for _ in range(0, N):
    l.append(int(input()))
l.reverse()

cnt = 0
for i in l:
    while((K//i) != 0):
        cnt += math.ceil(K//i)
        K = K - (math.ceil(K//i) * i)

print(cnt)
